import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

class StackedAutoencoder(nn.Module):
    def __init__(self, input_size, hidden_sizes):
        super(StackedAutoencoder, self).__init__()

        self.encoder_layers = nn.ModuleList()
        self.decoder_layers = nn.ModuleList()

        # Build encoder layers
        for i in range(len(hidden_sizes)):
            if i == 0:
                self.encoder_layers.append(nn.Linear(input_size, hidden_sizes[i]))
            else:
                self.encoder_layers.append(nn.Linear(hidden_sizes[i-1], hidden_sizes[i]))

        # Build decoder layers
        for i in reversed(range(len(hidden_sizes) - 1)):
            self.decoder_layers.append(nn.Linear(hidden_sizes[i+1], hidden_sizes[i]))
        self.decoder_layers.append(nn.Linear(hidden_sizes[0], input_size))


    def forward(self, x):
        # Encoder pass
        for i in range(len(self.encoder_layers)-1):
            layer = self.encoder_layers[i]
            x = torch.relu(layer(x))
        x = self.encoder_layers[-1](x)

        # Decoder pass
        for layer in range(len(self.decoder_layers)-1):
            layer = self.decoder_layers[i]
            x = torch.relu(layer(x))
        x = self.decoder_layers[-1](x)
        return x

    def pretrained(self, train_loader, lr=0.01, wd=1e-3, num_epochs=10):
        """
        Layer-wise pretraining of the SAE

        Args
        -----
        train_loader: the dataloader used for pretraining
        lr: learning rate for layerwise pretraining
        wd: weight-decay for layerwise pretraining
        num_epochs: number of epochs for training
        """
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.to(device)

        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(self.parameters(), lr=lr, weight_decay=wd)

        print("="*50)
        print("Begin layer-wise pretraining...")
        for i, layer in enumerate(self.encoder_layers):
            print(f"Pretraining Layer {i+1}/{len(self.encoder_layers)}")

            # Prepare a new model for the current layer
            model = nn.Sequential(*self.encoder_layers[:i+1], *self.decoder_layers[-(i+1):])
            model.to(device)

            for param in model.parameters():
                param.requires_grad = True

            # Training for the current layer
            for epoch in range(num_epochs):
                running_loss = 0.0
                for data in train_loader:
                    inputs, _ = data
                    inputs = inputs.view(-1, inputs.size(-1))
                    inputs = inputs.to(device)

                    optimizer.zero_grad()
                    outputs = model(inputs)
                    loss = criterion(outputs, inputs)
                    loss.backward()
                    optimizer.step()

                    running_loss += loss.item()

                print(f"Epoch {epoch+1}/{num_epochs}, Loss: {running_loss/len(train_loader)}")

            # Update the weights of the current layer in the original model
            self.encoder_layers[i].weight.data = model[i].weight.data
            self.encoder_layers[i].bias.data = model[i].bias.data
            self.decoder_layers[-i-1].weight.data = model[-i-1].weight.data
            self.decoder_layers[-i-1].bias.data = model[-i-1].bias.data

            # Freeze the weights of the current layer
            for param in self.encoder_layers[i].parameters():
                param.requires_grad = False

            for param in self.decoder_layers[-i-1].parameters():
                param.requires_grad = False

        # Unfreeze the weights
        for i in range(len(self.encoder_layers)):
            enc_layer = self.encoder_layers[i]
            for param in enc_layer.parameters():
                param.requires_grad = True
            dec_layer = self.decoder_layers[-i-1]
            for param in dec_layer.parameters():
                param.requires_grad = True

        print("Pretraining Complete")
        return nn.Sequential(*self.encoder_layers)

# Test on mnist
if __name__=="__main__":

    # flatten the data
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.view(-1)),  # Flatten the image,
    ])

    # Download and load the training data
    trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)

    # DataLoader
    batch_size = 64
    train_loader = DataLoader(trainset, batch_size=batch_size, shuffle=True)


    # Test
    input_size = 784  # For MNIST dataset
    hidden_sizes = [256, 128, 64]  # Define desired architecture
    autoencoder = StackedAutoencoder(input_size, hidden_sizes)
    print(autoencoder)
    
    # This is the encoder ready for use
    encoder = autoencoder.pretrained(train_loader, lr=1e-3, wd=0)