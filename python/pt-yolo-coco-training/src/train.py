import torch
import torch.optim as optim
import torchvision.transforms as transforms
from src.data_loader import load_dataset
from src.model import YOLOModel

def main():
    # Load dataset
    dataset = load_dataset(train=True)
    
    # Define model
    model = YOLOModel(num_classes=2)
    
    # Define loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
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