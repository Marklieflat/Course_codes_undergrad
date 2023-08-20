import  torch
from    torch import nn
from    torch import optim
from    torch.nn import functional as F
from    torch.utils.data import TensorDataset, DataLoader
from    torch import optim
from    torch.nn import functional as F
import  numpy as np
import copy
import scipy.io as scio
import os
from sklearn import preprocessing


from    learner import Learner
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

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#model = TimeSeriesLSTM(input_size, hidden_size, num_layers, num_classes)
model = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)

# Randomly generate the samples
num_samples = 10000
sequence_length = 4
input_size = 400
num_classes = 6

# Generate random input data
X_train = np.random.rand(num_samples, sequence_length, input_size)
#print(X_train[0,:,:])    shape: 13*140

# Generate random labels (integer values between 0 and num_classes-1)
y_train = np.random.randint(0, num_classes, size=(num_samples,))

X_test = np.random.rand(num_samples, sequence_length, input_size)
y_test = np.random.randint(0, num_classes, size=(num_samples,))

#train set
dir1 = "/home/student2/dongzewu/pacoh_nn/Widar/BVP/20181109-VS/6-link/user1"
list = os.listdir(dir1)
i=0
for file in list:
    csi_buff = scio.loadmat(dir1 + '/' + file)
    data = csi_buff['velocity_spectrum_ro']
    data_new=np.reshape(data,(400,data.shape[2]))
    data_new=data_new[:,:4]
    data_new = preprocessing.scale(data_new)
    X_train[i,:,:]=data_new.T
    y_train[i]=int(file.split('-')[1])-1
    i+=1
X_train=X_train[:i,:,:]
y_train=y_train[:i]


#test set
dir1 = "/home/student2/dongzewu/pacoh_nn/Widar/BVP/20181109-VS/6-link/user3"
list = os.listdir(dir1)
i=0
for file in list:
    csi_buff = scio.loadmat(dir1 + '/' + file)
    data = csi_buff['velocity_spectrum_ro']
    data_new=np.reshape(data,(400,data.shape[2]))
    data_new=data_new[:,:4]
    data_new = preprocessing.scale(data_new)
    X_test[i,:,:]=data_new.T
    y_test[i]=int(file.split('-')[1])-1
    i+=1
X_test=X_test[:i,:,:]
y_test=y_test[:i]

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
print("X_test_tensor shape:", X_test_tensor.shape)


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

num_tasks1 = 1000
num_tasks2 = 10
n_way = 5
k_shot = 2
query_size = 3

train_tasks = create_n_way_k_shot_tasks(X_train, y_train, num_tasks1, n_way, k_shot, query_size)
test_tasks = create_n_way_k_shot_tasks(X_test, y_test, num_tasks2, n_way, k_shot, query_size)

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
#train_dataloader = data_utils.DataLoader(train_dataset, batch_size=task_num, shuffle=True) #batch size is the number of tasks
test_dataloader = data_utils.DataLoader(test_dataset, batch_size=1, shuffle=False) #batch size is the number of tasks


# Create a Dataset and DataLoader
#train_dataset = data_utils.TensorDataset(X_train_tensor, y_train_tensor)
#train_dataloader = data_utils.DataLoader(train_dataset, batch_size=64, shuffle=True)

# Define the loss function and the optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

update_lr=0.01


# Training loop
def train(model, criterion, optimizer, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        train_dataloader = data_utils.DataLoader(train_dataset, batch_size=task_num, shuffle=True) #batch size is the number of tasks
        for batch_idx, ((support_X, support_y), (query_X, query_y)) in enumerate(train_dataloader):
            # batch_idx ranges from 0 to 19
            spt_x=support_X    #size: (5,10,4,400)  (task_num, n_way*k_shot, sequence_length, features)
            spt_y=support_y    #size: (5,10) (task_num, n_way*k_shot)
            qry_x=query_X
            qry_y=query_y
            losses_list=[]
            gradients=0
            for i in range(spt_x.shape[0]):
                outputs=model(spt_x[i,:,:,:])   #spt_x[i,:,:,:]: (10,4,400)
                loss = criterion(outputs, spt_y[i,:])
                model.zero_grad()
                gradients = torch.autograd.grad(loss, model.parameters(), create_graph=True)
                model_param=model.get_parameters()
                updated_params = {}
                for (name, param),grad in zip(model_param.items(),gradients):
                    updated_params[name] = param - update_lr * grad
                
                temp_model=copy.deepcopy(model)
                outputs_q=temp_model(qry_x[i,:,:,:],parameters=updated_params)
 
                #outputs_q=model(qry_x[i,:,:,:],parameters=updated_params)
                #loss_q = criterion(outputs_q, qry_y[i,:])
                loss_q=F.cross_entropy(outputs_q, qry_y[i,:])
                losses_list.append(loss_q)
                ######################??????????????? model.parameters()   allow_unsed????
                gradients_q = torch.autograd.grad(loss_q, model.parameters(), retain_graph=True, allow_unused=True)
                gradients+=gradients_q
            model.zero_grad()

            
            with torch.no_grad():
                for param, grad_q in zip(model.parameters(), gradients):
                    param -= optimizer.param_groups[0]['lr'] * grad_q
        
        test(model,test_dataloader, criterion, optimizer)

        #Start test and fine-tuning
        #print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")



def test(model, dataloader, criterion, optimizer):
    model.eval()
    correct = []
    for batch_idx, ((support_X, support_y), (query_X, query_y)) in enumerate(test_dataloader):
        # Unpack the batch
        spt_x=support_X    #size: (5,10,13,400)
        spt_y=support_y    #size: (5,10)
        qry_x=query_X
        qry_y=query_y
        gradients=0
        for i in range(spt_x.shape[0]):
            #model_copy=copy.deepcopy(model)
            outputs=model(spt_x[i,:,:,:])
            loss = criterion(outputs, spt_y[i,:])
            model.zero_grad()
            gradients = torch.autograd.grad(loss, model.parameters(), create_graph=True)
            model_param=model.get_parameters()
            updated_params = {}
            for (name, param),grad in zip(model_param.items(),gradients):
                updated_params[name] = param - update_lr * grad
            temp_model=copy.deepcopy(model)
            outputs_q=temp_model(qry_x[i,:,:,:],parameters=updated_params)
            loss_q = criterion(outputs_q, qry_y[i,:])
            print('outputs_q:', outputs_q)
            pred = outputs_q.max(1, keepdim=True)[1]
            print('pred:', pred)
            print('qry_y[i,:]:', qry_y[i,:])

            correct.append(pred.eq(qry_y[i,:]).sum()/(n_way*query_size))
            #correct += pred.eq(qry_y[i,:].view_as(pred)).sum().item()
        #correct /= spt_x.shape[0]
    print('Accuracy:', np.mean(correct)/(n_way*query_size))

# Training loop
def train(model, criterion, optimizer, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        train_dataloader = data_utils.DataLoader(train_dataset, batch_size=task_num, shuffle=True) #batch size is the number of tasks
        for batch_idx, ((support_X, support_y), (query_X, query_y)) in enumerate(train_dataloader):
            # batch_idx ranges from 0 to 19
            spt_x=support_X    #size: (5,10,4,400)  (task_num, n_way*k_shot, sequence_length, features)
            spt_y=support_y    #size: (5,10) (task_num, n_way*k_shot)
            qry_x=query_X
            qry_y=query_y
            losses_list=[]
            for i in range(spt_x.shape[0]):
                outputs=model(spt_x[i,:,:,:])   #spt_x[i,:,:,:]: (10,4,400)
                loss = F.cross_entropy(outputs, spt_y[i,:])
                model.zero_grad()
                losses_list.append(loss)
            losses=sum(losses_list)/len(losses_list)
            losses.backward()
        
        test(model,test_dataloader, criterion, optimizer)

        #Start test and fine-tuning
        #print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")



def test(model, dataloader, criterion, optimizer):
    model.eval()
    correct = []
    for batch_idx, ((support_X, support_y), (query_X, query_y)) in enumerate(test_dataloader):
        # Unpack the batch
        spt_x=support_X    #size: (5,10,13,400)
        spt_y=support_y    #size: (5,10)
        qry_x=query_X
        qry_y=query_y
        gradients=0
        for i in range(spt_x.shape[0]):
            #model_copy=copy.deepcopy(model)
            outputs_q=model(spt_x[i,:,:,:])
            loss_q = F.cross_entropy(outputs_q, spt_y[i,:])
            print('outputs_q:', outputs_q)
            pred = outputs_q.max(1, keepdim=True)[1]
            print('pred:', pred)
            print('qry_y[i,:]:', spt_y[i,:])

            correct.append(pred.eq(spt_y[i,:]).sum()/(n_way*query_size))
            #correct += pred.eq(qry_y[i,:].view_as(pred)).sum().item()
        #correct /= spt_x.shape[0]
    print('Accuracy:', np.mean(correct)/(n_way*query_size))


num_epochs = 30
train(model, criterion, optimizer, num_epochs)



def main():
    pass


if __name__ == '__main__':
    main()
