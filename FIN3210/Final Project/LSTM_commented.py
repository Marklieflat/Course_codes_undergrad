import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import time
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve, precision_score, recall_score, f1_score, roc_curve, roc_auc_score
from metrics import mape, pearson_correlation, theil_u

# Set the device to GPU if CUDA is available, otherwise use CPU
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# Read the dataset from a CSV file
df = pd.read_csv('top_15.csv')

# Filter the dataframe for a specific 'code'
df = df.loc[df['code'] == 12]

# Split the data into training and testing sets based on index
train_data = df.iloc[:1500]
test_data = df.iloc[1500:]

# Extract the features (last 6 columns) and the target (3rd column) from the dataset
X_train = train_data.iloc[:, -6:].values.astype(np.float32)
y_train = train_data.iloc[:, 2].values.astype(np.float32)
X_test = test_data.iloc[:, -6:].values.astype(np.float32)
y_test = test_data.iloc[:, 2].values.astype(np.float32)

# Define a custom Dataset class for the training data
class TrainDataset(Dataset):
    def __init__(self, data, label=np.nan, window_size=16, stride=1):
        # Initialization method where data is preprocessed into sliding window sequences
        self.window_size = window_size
        self.stride = stride
        self.data = data
        self.label = label
        self.sequences = []
        self.labels = []
        i = 0
        while i < len(self.data) - self.window_size + 1:
            sequence = self.data[i:i+self.window_size]
            label = self.label[i + self.window_size - 1]
            if len(sequence) == self.window_size:
                self.sequences.append(sequence)
                self.labels.append(label)
            i += self.stride

    def __getitem__(self, index):
        # Method to get a single window sequence and its corresponding label
        sequence = self.sequences[index]
        label = self.labels[index]
        return sequence, label

    def __len__(self):
        # Method to get the total number of window sequences
        return len(self.sequences)

# Define a custom Dataset class for the testing data (without labels)
class TestDataset(Dataset):
    def __init__(self, data, window_size = 16, stride = 1):
        self.window_size = window_size
        self.stride = stride
        self.data = data
        self.sequences = []
        i = 0
        while i < len(self.data)-self.window_size+1:
            sequence = self.data[i:i+self.window_size]
            if len(sequence) == self.window_size:
                self.sequences.append(sequence)
            i += self.stride

    def __getitem__(self, index):
            sequence = self.sequences[index]
            return sequence

    def __len__(self):
        return len(self.sequences)

# Define a LSTM model class
class LSTM(nn.Module):
    def __init__(self, input_size: int, hidden_size: int, num_layers: int, num_classes: int, learning_rate: float = 1e-2):
        super(LSTM, self).__init__()
        self.lr = learning_rate
        self.num_layers = num_layers
        self.hidden_size = hidden_size
        # LSTM layer
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        # Fully connected layer
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # Forward pass through the network
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out)
        out = out[:, -1, :]
        return out

# Initialize the LSTM model
model = LSTM(
    input_size=6,
    hidden_size=16,
    num_layers=2,
    num_classes=1,
).to(device)

# Training hyperparameters
batch_size = 16
max_epoch = 50

# Initialize Datasets and DataLoaders for training and testing
train_dataset = TrainDataset(X_train, y_train, window_size=16)
test_dataset = TrainDataset(X_test, y_test, window_size=16)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False, drop_last=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, drop_last=False)

# Initialize the optimizer and loss function
optimizer = torch.optim.Adam(model.parameters(), lr=0.03)
loss_func = nn.MSELoss()

# Begin training
time_start = time.time()
train_loss_all = []
model.train()
for epoch in range(max_epoch):
    train_loss = 0
    train_num = 0
    for step, (b_x, b_y) in enumerate(train_loader):
        b_x = b_x.to(device)
        b_y = b_y.to(device)
        b_y = b_y.view(-1, 1)
        output = model(b_x)
        loss = loss_func(output, b_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_loss += loss.item() * b_x.size(0)
        train_num += b_x.size(0)
    if (epoch+1) % 5 == 0:
        print(f'Epoch{epoch+1}/{max_epoch}: Loss:{train_loss/train_num}')
    train_loss_all.append(train_loss/train_num)

time_end = time.time()
print("Training time is: ", time_end-time_start)
torch.save(model.state_dict(), 'LSTM_model.pt')

# Load the trained model for evaluation
model.load_state_dict(torch.load('LSTM_model.pt'))

# Evaluate the model
model.eval()
res = []
true_label = []
with torch.no_grad():
    test_loss = 0
    test_num = 0
    for b_x, b_y in test_loader:
        b_x = b_x.to(device)
        b_y = b_y.to(device)
        b_y = b_y.view(-1, 1)
        output = model(b_x)
        res.append(output.view(-1).tolist())
        true_label.append(b_y.view(-1).tolist())
        loss = loss_func(output, b_y)
        test_loss += loss.item() * b_x.size(0)
        test_num += b_x.size(0)
    print(f'Test Loss: {test_loss/test_num}')
res = np.concatenate(np.array(res))
true_label = np.concatenate(np.array(true_label))

# Calculate and print the evaluation metrics
print('MAPE in Percentage: ', mape(true_label, res))
print('Pearson Correlation: ', pearson_correlation(true_label, res))
print('Theil-U: ', theil_u(true_label, res))
