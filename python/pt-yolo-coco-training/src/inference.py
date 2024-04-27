import torch
from src.model import YOLOModel

def main(image_path):
    pass
    # Load saved model
    model = YOLOv4Tiny()
    model.load_state_dict(torch.load("models/"))
    model.eval()
    
    # Perform inference on image
    with torch.no_grad():
        outputs = model(image_path)
    
    # Process outputs
    pass