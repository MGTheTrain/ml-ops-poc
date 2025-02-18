import unittest
import torch
from models.yolo_v4_tiny import YOLOv4Tiny


class TestYOLOv4Tiny(unittest.TestCase):
    
    def test_build(self):
        yolo_model = YOLOv4Tiny()
        model = yolo_model.build(num_classes=2)
        
        # Check that the model is an instance of torch.nn.Module
        self.assertIsInstance(model, torch.nn.Module)
        
        # Get children of the model (conv_layers and yolo_layers)
        children = list(model.children())
        
        # Check that the model contains 2 parts: conv_layers and yolo_layers
        self.assertEqual(len(children), 2)
        
        # Check types of the parts in the model (conv_layers and yolo_layers)
        self.assertIsInstance(children[0], torch.nn.ModuleList)  # conv_layers
        self.assertIsInstance(children[1], torch.nn.ModuleList)  # yolo_layers
        
        # Check number of layers in conv_layers and yolo_layers
        self.assertEqual(len(children[0]), 45)  # Assuming 45 layers in conv_layers
        self.assertEqual(len(children[1]), 7)   # Assuming 7 layers in yolo_layers
        
        # Verify types of layers within conv_layers
        self.assertIsInstance(children[0][0], torch.nn.Conv2d)
        self.assertIsInstance(children[0][1], torch.nn.BatchNorm2d)
        self.assertIsInstance(children[0][2], torch.nn.LeakyReLU)
        self.assertIsInstance(children[0][3], torch.nn.Conv2d)
        
        # Verify properties of the first YOLO layer
        self.assertIsInstance(children[1][0], torch.nn.Conv2d)
        self.assertEqual(children[1][0].in_channels, 512)  # Input channels from conv_layers
        self.assertEqual(children[1][0].out_channels, 256)  # Output channels of YOLO layer
        
        # Verify the final YOLO layer (output layer)
        self.assertIsInstance(children[1][6], torch.nn.Conv2d)
        self.assertEqual(children[1][6].out_channels, 10)  # 10 = 2 classes * (4 + 1) (bbox + objectness)
        
        # Check if the model's forward pass runs without errors (basic test)
        x = torch.randn(1, 3, 416, 416)  # Input with batch size 1 and image size 416x416
        output, route_1 = model(x)
        
        # Check output shape: Should be (batch_size, num_classes * 5, grid_size, grid_size)
        # The output should have a size like [1, 10, 114, 114] for 2 classes (as per YOLOv4 Tiny configuration)
        self.assertEqual(output.shape, (1, 10, 114, 114))


if __name__ == "__main__":
    unittest.main()
