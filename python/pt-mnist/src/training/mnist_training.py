import torch
import torch.optim as optim
import torch.nn as nn
from data_loaders.mnist_data_loader import MNISTDataLoader
from models.simple_nn import SimpleNN
from training.training_interface import TrainingInterface


class MNISTTraining(TrainingInterface):
    def train(
        self, model_path: str = "../models/mnist_model.h5", data_set_path: str = ""
    ) -> None:
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load(
            data_set_path=data_set_path
        )

        simple_nn = SimpleNN()
        model = simple_nn.build()

        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        model.train()
        for epoch in range(10):
            optimizer.zero_grad()
            outputs = model(x_train)
            loss = criterion(outputs, y_train)
            loss.backward()
            optimizer.step()
            print(f"Epoch {epoch+1}, Loss: {loss.item()}")

        torch.save(model.state_dict(), model_path)
