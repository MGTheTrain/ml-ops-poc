import torch
from models.yolo_v4_tiny import YOLOv4Tiny
from inferences.inference_interface import InferenceInterface
from PIL import Image
from torchvision import transforms

class YOLOv4TinyInference(InferenceInterface):
    def infer(self, model_path: str = "../models/yolov4tiny_model.pth", image_path: str = "") -> None:
        # Load the image
        image = Image.open(image_path).convert("RGB")

        # Define transformations (resize, normalize, convert to tensor)
        transform = transforms.Compose([
            transforms.Resize((416, 416)),  # YOLOv4 typically uses 416x416 input size
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Adjust normalization for your model
        ])

        # Apply the transformations to the image
        image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

        # Load the model
        model = YOLOv4Tiny(num_classes=80)  # Adjust the number of classes as needed
        model.load_state_dict(torch.load(model_path))
        model.eval()

        # Perform inference on the image
        with torch.no_grad():
            outputs, _ = model(image_tensor)

        # Process the outputs (for YOLO models, this involves post-processing to extract boxes, labels, and scores)
        print(outputs)
        
        # Add post-processing logic for bounding boxes, confidence scores, and class labels if needed
        # This may involve non-maximum suppression, thresholding, etc.
        pass