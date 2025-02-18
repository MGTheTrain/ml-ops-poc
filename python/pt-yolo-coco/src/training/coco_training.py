import torch
import torch.optim as optim
import torch.nn as nn
from src.data_loaders.coco_data_loader import COCODataLoader 
from src.models.yolo_v4_tiny import YOLOv4Tiny 
from src.training.training_interface import TrainingInterface

class COCOTraining(TrainingInterface):
    def train(self, model_path: str = "../models/yolov4tiny_model.pth", data_set_path: str = "") -> None:
        # Load COCO dataset using COCODataLoader
        data_loader = COCODataLoader()
        train_loader, val_loader = data_loader.load(data_set_path=data_set_path)

        # Initialize YOLOv4Tiny model
        model = YOLOv4Tiny(num_classes=80)  # Change 80 to match the number of classes in your case

        # Define loss function and optimizer
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        # Training loop
        model.train()
        num_epochs = 10
        for epoch in range(num_epochs):
            for batch_idx, (images, targets) in enumerate(train_loader):
                # Forward pass
                outputs, _ = model(images)  # Assuming model returns both outputs and route_1
                loss = criterion(outputs, targets)

                # Backward pass and optimization
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            print(f"Epoch {epoch+1}, Loss: {loss.item()}")

        # Save trained model
        torch.save(model.state_dict(), model_path)
