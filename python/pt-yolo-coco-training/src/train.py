import torch
import torch.optim as optim
import torch.nn as nn
from src.data_loader import load_dataset
from src.model import YOLOv4Tiny

def main():
    # Load dataset
    dataset = load_dataset(train=True)
    
    # Define model
    model = YOLOv4Tiny(num_classes=80)
    
    # Define loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    num_epochs=10
    # Training loop
    for epoch in range(num_epochs):
        for batch_idx, (images, targets) in enumerate(dataset):
            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, targets)
            
            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    # Save trained model
    torch.save(model.state_dict(), "models")