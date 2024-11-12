import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import time
from torch.utils.data import Dataset, DataLoader
from metrics import pearson_correlation, theil_u, mase
from SAE import StackedAutoencoder
from WT import denoise_factors_with_wavelet
from matplotlib import pyplot as plt

device = "cuda:0" if torch.cuda.is_available() else "cpu"

torch.manual_seed(0)
np.random.seed(0)
torch.backends.cudnn.deterministic = True

class TrainDataset(Dataset):
    def __init__(self, data, label=np.nan, window_size = 16, stride = 1):
        self.window_size = window_size
        self.stride = stride
        self.data = data
        self.label = label
        self.sequences = []
        self.labels = []
        i = 0
        while i < len(self.data)-self.window_size+1:
            sequence = self.data[i:i+self.window_size]
            label = self.label[i + self.window_size-1]
            if len(sequence) == self.window_size:
                self.sequences.append(sequence)
                self.labels.append(label)
            i += self.stride

    def __getitem__(self, index):
        sequence = self.sequences[index]
        label = self.labels[index]
        return sequence, label

    def __len__(self):
        return len(self.sequences)

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
    
    
class LSTM(nn.Module):
    def __init__(self, input_size: int, hidden_size: int, num_layers: int, num_classes: int, learning_rate: float = 1e-2):
        super(LSTM, self).__init__()
        self.lr = learning_rate
        self.num_layers = num_layers
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out)
        out = out[:, -1, :]
        return out
    
batch_size = 512
max_epoch = 30

ori_df = pd.read_csv('top_10_v5_selected_normalized.csv')

# print(df.columns.unique())

for code in ori_df.code.unique():
    df = ori_df.loc[ori_df['code'] == code].reset_index(drop=True)
    df['cumret'] = (1 + df['ret']).cumprod()-1
    """
    Denoised with wavelet
    """
    # denoised_df = denoise_factors_with_wavelet(df, df.columns.tolist()[3:])
    # denoised_df.reset_index(drop=True, inplace=True)
    # df = pd.concat([df.iloc[:, :3], denoised_df], axis=1)

    # df = pd.read_csv('portfolio_wt.csv')

    # df = pd.read_csv('normalized_portfolio.csv')
    """
    Training and Testing
    """
    time_start = time.time()

    train_data = df
    test_data = df.iloc[1500:]

    X_train = train_data.iloc[:, -25:-1].values.astype(np.float32)
    y_train = train_data['cumret'].values.astype(np.float32)
    X_test = test_data.iloc[:, -25:-1].values.astype(np.float32)
    y_test = test_data['cumret'].values.astype(np.float32)

    train_dataset = TrainDataset(X_train, y_train, window_size=2)
    test_dataset = TrainDataset(X_test, y_test, window_size=2)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False, drop_last=False)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, drop_last=False)

    autoencoder = StackedAutoencoder(input_size=24, hidden_sizes=[20, 16, 8])
    train_encoder = autoencoder.pretrained(train_loader, lr=0.01, wd=0)
    test_encoder = autoencoder.pretrained(test_loader, lr=0.01, wd=0)

    model = LSTM(
            input_size=8,
            hidden_size=16,
            num_layers=2,
            num_classes=1,
        ).to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr = 0.03)
    loss_func = nn.MSELoss()
    train_loss_all = []

    model.train()
    for epoch in range(max_epoch):
        train_loss = 0
        train_num = 0
        for step, (b_x, b_y) in enumerate(train_loader):
            # print(b_y)
            # print(b_y.shape)
            b_x = b_x.to(device)
            b_x = train_encoder(b_x)
            b_y = b_y.to(device)
            b_y = b_y.view(-1, 1)
            output = model(b_x)
            # print(output.shape)
            # print(b_y.shape)
            loss = loss_func(output, b_y)
            optimizer.zero_grad()
            # print(model.lstm.bias_hh_l1)
            loss.backward()
            optimizer.step()
            train_loss += loss.item() * b_x.size(0)
            train_num += b_x.size(0)
        if (epoch+1) % 5 == 0:
            print(f'Epoch{epoch+1}/{max_epoch}: Loss:{train_loss/train_num}')
        train_loss_all.append(train_loss/train_num)
        # print(model.lstm.weight_ih_l0)
        # for name, param in model.named_parameters():
        #     if param.requires_grad:
        #         print(name, param.grad)

    time_end = time.time()
    print("Training time is: ", time_end-time_start)
    # print(train_loss_all)
    torch.save(model.state_dict(), 'LSTM_model.pt')
    model.load_state_dict(torch.load('LSTM_model.pt'))


    model.eval()
    res = []
    true_label = []
    with torch.no_grad():
        test_loss = 0
        test_num = 0
        for b_x, b_y in test_loader:
            b_x = b_x.to(device)
            b_x = test_encoder(b_x)
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
    # print(res.shape)
    # print("\n")
    # print(true_label.shape)
    res_frame = pd.DataFrame({'pred': res, 'true': true_label})
    code_date = test_data.iloc[-202:, :2].reset_index(drop=True)
    res_final = pd.concat([code_date, res_frame], axis=1)

    res_final.to_csv(f'LSTM_result_{code}.csv', index=False)


    print('MASE: ', mase(true_label, res))
    print('Pearson Correlation: ', pearson_correlation(true_label, res))
    print('Theil-U: ', theil_u(true_label, res))
