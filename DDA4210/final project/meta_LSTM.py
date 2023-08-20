import torch
from torch import nn
from torch import optim
from torch.nn import functional as F
from torch.utils.data import TensorDataset, DataLoader
from torch import optim
import numpy as np
import copy

# from    learner import Learner
from copy import deepcopy
import torch.utils.data as data_utils

class TimeSeriesLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(TimeSeriesLSTM, self).__init__()

        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.num_classes = num_classes

        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x, parameters=None):
        if parameters is not None:
            model_copy = copy.deepcopy(self)
            model_copy.load_state_dict(parameters)
            return model_copy.forward(x)

        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])

        return out

    def get_parameters(self):
        return self.state_dict()



# Parameters
input_size = 400         # The number of input features per time step
sequence_length = 13     # The number of time steps in the sequence
hidden_size = 128        # The number of features in the hidden state
num_layers = 2           # The number of stacked LSTM layers
num_classes = 6          # The number of output classes

# Create the model
model = TimeSeriesLSTM(input_size, hidden_size, num_layers, num_classes)

# Randomly generate the samples
num_samples = 1000
sequence_length = 13
input_size = 400
num_classes = 6

# Generate random input data
X_train = np.random.rand(num_samples, sequence_length, input_size)
#print(X_train[0,:,:])    shape: 13*140

# Generate random labels (integer values between 0 and num_classes-1)
y_train = np.random.randint(0, num_classes, size=(num_samples,))

# Print the shapes of X_train and y_train
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)



# Assuming your data is stored in X_train, y_train (numpy arrays)
# Convert your data into PyTorch tensors
X_train_tensor = torch.from_numpy(X_train).float()
y_train_tensor = torch.from_numpy(y_train).long()
print("X_train_tensor shape:", X_train_tensor.shape)




# Generate the task
def create_n_way_k_shot_tasks(X, y, num_tasks, n_way, k_shot, query_size):
    tasks = []
    unique_classes = np.unique(y)
    
    if n_way > len(unique_classes):
        raise ValueError("n_way should be less than or equal to the number of unique classes in the dataset.")

    for _ in range(num_tasks):
        task_classes = np.random.choice(unique_classes, n_way, replace=False)
        support_set = []
        support_labels = []
        query_set = []
        query_labels = []

        for class_label in task_classes:
            class_indices = np.where(y == class_label)[0]
            class_examples = X[class_indices]

            if k_shot + query_size > len(class_examples):
                raise ValueError("k_shot + query_size should be less than or equal to the number of examples per class.")

            selected_indices = np.random.choice(range(len(class_examples)), k_shot + query_size, replace=False)
            support_indices = selected_indices[:k_shot]
            query_indices = selected_indices[k_shot:]

            support_set.extend(class_examples[support_indices])
            support_labels.extend([class_label] * k_shot)
            query_set.extend(class_examples[query_indices])
            query_labels.extend([class_label] * query_size)

        tasks.append(((np.array(support_set), np.array(support_labels)), (np.array(query_set), np.array(query_labels))))

    return tasks

num_tasks = 100
n_way = 5
k_shot = 2
query_size = 3

tasks = create_n_way_k_shot_tasks(X_train, y_train, num_tasks, n_way, k_shot, query_size)




class MetaLearningDataset(data_utils.Dataset):
    def __init__(self, tasks):
        self.tasks = tasks

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, index):
        support_set, query_set = self.tasks[index]
        support_X, support_y = support_set
        query_X, query_y = query_set

        support_X = torch.from_numpy(support_X).float()
        support_y = torch.from_numpy(support_y).long()
        query_X = torch.from_numpy(query_X).float()
        query_y = torch.from_numpy(query_y).long()

        return (support_X, support_y), (query_X, query_y)

train_dataset = MetaLearningDataset(tasks)
task_num=5
train_dataloader = data_utils.DataLoader(train_dataset, batch_size=task_num, shuffle=True) #batch size is the number of tasks



# Create a Dataset and DataLoader
#train_dataset = data_utils.TensorDataset(X_train_tensor, y_train_tensor)
#train_dataloader = data_utils.DataLoader(train_dataset, batch_size=64, shuffle=True)

# Define the loss function and the optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

update_lr=0.01

# Training loop
def train(model, dataloader, criterion, optimizer, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        for batch_idx, ((support_X, support_y), (query_X, query_y)) in enumerate(train_dataloader):
            # Unpack the batch
            spt_x=support_X    #size: (5,10,13,400)
            spt_y=support_y    #size: (5,10)
            qry_x=query_X
            qry_y=query_y
            losses_list=[]
            for i in range(spt_x.shape[0]):
                #model_copy=copy.deepcopy(model)
                outputs=model(spt_x[i,:,:])
                loss = criterion(outputs, spt_y[i,:])
                model.zero_grad()
                gradients = torch.autograd.grad(loss, model.parameters(), create_graph=True)
                model_param=model.get_parameters()
                updated_params = {}
                for (name, param),grad in zip(model_param.items(),gradients):
                    updated_params[name] = param - update_lr * grad
                '''
                for param, grad in zip(model.parameters(), gradients):
                    updated_params.append(param - update_lr * grad)'''
                outputs_q=model(qry_x[i,:,:],parameters=updated_params)
                loss_q = criterion(outputs_q, qry_y[i,:])
                losses_list.append(loss_q)
            total_loss=sum(losses_list)/task_num
            model.zero_grad()
            #torch.autograd.set_detect_anomaly(True)
            total_loss.backward()
            #optimizer.step()

        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

num_epochs = 30
train(model, train_dataloader, criterion, optimizer, num_epochs)


'''
def train(model, dataloader, criterion, optimizer, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        for batch_idx, ((support_X, support_y), (query_X, query_y)) in enumerate(train_dataloader):
            # Unpack the batch
            spt_x = support_X    # size: (5,10,13,400)
            spt_y = support_y    # size: (5,10)
            qry_x = query_X
            qry_y = query_y
            losses_list = []
            for i in range(spt_x.shape[0]):
                outputs = model(spt_x[i, :, :])
                loss = criterion(outputs, spt_y[i, :])
                model.zero_grad()

                # Compute gradients using torch.autograd.grad()
                gradients = torch.autograd.grad(loss, model.parameters(), create_graph=True)
                updated_params = []
                for param, grad in zip(model.parameters(), gradients):
                    updated_params.append(param - update_lr * grad)

                # Load updated parameters into the model_copy
                for updated_param, param in zip(updated_params, model.parameters()):
                    param.data = updated_param.data

                outputs_q = model(qry_x[i, :, :], parameters=model.get_parameters(), use_temp_model=True)
                loss_q = criterion(outputs_q, qry_y[i, :])
                losses_list.append(loss_q)
            total_loss = sum(losses_list) / task_num
            model.zero_grad()
            total_loss.backward()
            optimizer.step()

        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

num_epochs = 30
train(model, train_dataloader, criterion, optimizer, num_epochs)'''



def main():
    pass


if __name__ == '__main__':
    main()
