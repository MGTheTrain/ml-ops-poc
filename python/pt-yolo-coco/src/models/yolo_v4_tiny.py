import torch.nn as nn
from src.models.model_interface import ModelInterface

# Refer to: https://github.com/MGTheTrain/python-yolo-training-with-jupyter-notebooks/blob/main/data-custom/yolov4-tiny-custom.cfg

class YOLOv4Tiny(ModelInterface):
    def build(self, num_classes=2):
        class YOLOv4TinyModel(nn.Module):
            def __init__(self, num_classes=2):
                super(YOLOv4TinyModel, self).__init__()

                # Define convolutional layers
                self.conv_layers = nn.ModuleList([
                    nn.Conv2d(3, 32, kernel_size=3, stride=2, padding=1),
                    nn.BatchNorm2d(32),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),
                    nn.BatchNorm2d(64),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(64),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(64, 32, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(32),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(32, 32, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(32),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(32, 64, kernel_size=1, stride=1, padding=1),
                    nn.BatchNorm2d(64),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(128),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(128, 64, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(64),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(64),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(64, 128, kernel_size=1, stride=1, padding=1),
                    nn.BatchNorm2d(128),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(256),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(256, 128, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(128),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(128),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(128, 256, kernel_size=1, stride=1, padding=1),
                    nn.BatchNorm2d(256),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(512),
                    nn.LeakyReLU(0.1, inplace=True)
                ])

                # Define YOLO layers
                self.yolo_layers = nn.ModuleList([
                    nn.Conv2d(512, 256, kernel_size=1, stride=1, padding=1),
                    nn.BatchNorm2d(256),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1),
                    nn.BatchNorm2d(512),
                    nn.LeakyReLU(0.1, inplace=True),

                    nn.Conv2d(512, num_classes * 5, kernel_size=1, stride=1, padding=1)
                ])

            def forward(self, x):
                # Pass through convolutional layers
                for layer in self.conv_layers:
                    x = layer(x)

                route_1 = x

                # Pass through YOLO layers
                for layer in self.yolo_layers:
                    x = layer(x)

                return x, route_1

        # Create and return model
        model = YOLOv4TinyModel(num_classes)
        print(model)
        return model
