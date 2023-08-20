import  torch
from    torch import nn
from    torch import optim
from    torch.nn import functional as F
from    torch.utils.data import TensorDataset, DataLoader
from    torch import optim
import  numpy as np
import copy

# from    learner import Learner
from    copy import deepcopy
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
        '''
        if parameters is not None:
            model_copy = copy.deepcopy(self)
            model_copy.load_state_dict(parameters)
            return model_copy.forward(x)'''
        if parameters is not None:
            self.load_state_dict(parameters)

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
X_test = np.random.rand(num_samples, sequence_length, input_size)
#print(X_train[0,:,:])    shape: 13*140

# Generate random labels (integer values between 0 and num_classes-1)
y_train = np.random.randint(0, num_classes, size=(num_samples,))
y_test = np.random.randint(0, num_classes, size=(num_samples,))

# Print the shapes of X_train and y_train
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)



# Assuming your data is stored in X_train, y_train (numpy arrays)
# Convert your data into PyTorch tensors
X_train_tensor = torch.from_numpy(X_train).float()
y_train_tensor = torch.from_numpy(y_train).long()
X_test_tensor = torch.from_numpy(X_test).float()
y_test_tensor = torch.from_numpy(y_test).long()
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

train_tasks = create_n_way_k_shot_tasks(X_train, y_train, num_tasks, n_way, k_shot, query_size)
test_tasks = create_n_way_k_shot_tasks(X_test, y_test, 10 , n_way, k_shot, query_size)



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

train_dataset = MetaLearningDataset(train_tasks)
test_dataset = MetaLearningDataset(test_tasks)
task_num=5
train_dataloader = data_utils.DataLoader(train_dataset, batch_size=task_num, shuffle=True) #batch size is the number of tasks
test_dataloader = data_utils.DataLoader(test_dataset, batch_size=task_num, shuffle=True)


# Create a Dataset and DataLoader
#train_dataset = data_utils.TensorDataset(X_train_tensor, y_train_tensor)
#train_dataloader = data_utils.DataLoader(train_dataset, batch_size=64, shuffle=True)

# Define the loss function and the optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

update_lr=0.01

def test(model, dataloader, criterion, optimizer):
    model.eval()
    correct = 0
    for batch_idx, ((support_X, support_y), (query_X, query_y)) in enumerate(test_dataloader):
        # Unpack the batch
        spt_x=support_X    #size: (5,10,13,400)
        spt_y=support_y    #size: (5,10)
        qry_x=query_X
        qry_y=query_y
        gradients=0
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
            temp_model=copy.deepcopy(model)
            outputs_q=temp_model(qry_x[i,:,:],parameters=updated_params)
            loss_q = criterion(outputs_q, qry_y[i,:])
            pred = outputs_q.max(1, keepdim=True)[1]
            correct += pred.eq(qry_y[i,:].view_as(pred)).sum().item()
        correct /= len(test_dataloader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
    loss_q, correct, len(test_dataloader.dataset),
    100. * correct / len(test_dataloader.dataset)))


# Training loop
def train(model, train_dataloader, test_dataloader, criterion, optimizer, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        for batch_idx, ((support_X, support_y), (query_X, query_y)) in enumerate(train_dataloader):
            # Unpack the batch
            spt_x=support_X    #size: (5,10,13,400)
            spt_y=support_y    #size: (5,10)
            qry_x=query_X
            qry_y=query_y
            losses_list=[]
            gradients=0
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
                temp_model=copy.deepcopy(model)
                outputs_q=temp_model(qry_x[i,:,:],parameters=updated_params)
                loss_q = criterion(outputs_q, qry_y[i,:])
                gradients_q = torch.autograd.grad(loss_q, temp_model.parameters(), retain_graph=True)#, allow_unused=True)
                gradients+=gradients_q

                #losses_list.append(loss_q)
            #total_loss=sum(losses_list)/task_num
            # for name, parms in model.named_parameters():	
            #     print('-->name:', name)
            #     print('-->para:', parms[0])
            #     # print('-->grad_requires:',parms.requires_grad)
            #     # print('-->grad_value:',parms.grad)
            #     print("===")
            model.zero_grad()

            with torch.no_grad():
                for param, grad_q in zip(model.parameters(), gradients):
                    param -= optimizer.param_groups[0]['lr'] * grad_q
            
        test(model,test_dataloader, criterion, optimizer)


        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

num_epochs = 10
train(model, train_dataloader, test_dataloader, criterion, optimizer, num_epochs)

# def main():
#     pass


# if __name__ == '__main__':
#     main()
