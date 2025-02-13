import torch.nn as nn
from models.model_interface import ModelInterface


class SimpleNN(ModelInterface):
    def build(self):
        class SimpleNN(nn.Module):
            def __init__(self):
                super(SimpleNN, self).__init__()
                self.flatten = nn.Flatten()
                self.fc1 = nn.Linear(28 * 28, 128)
                self.relu = nn.ReLU()
                self.fc2 = nn.Linear(128, 10)
                self.softmax = nn.Softmax(dim=1)

            def forward(self, x):
                x = self.flatten(x)
                x = self.fc1(x)
                x = self.relu(x)
                x = self.fc2(x)
                x = self.softmax(x)
                return x

        model = SimpleNN()
        print(model)
        return model
