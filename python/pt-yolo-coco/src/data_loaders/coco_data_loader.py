import os
import torch
import requests
import zipfile
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import CocoDetection
from typing import Tuple
from data_loaders.data_loader_interface import DataLoaderInterface


class COCODataLoader(DataLoaderInterface):
    def load(self, data_set_path: str = "") -> Tuple[Tuple, Tuple]:
        """
        Loads the COCO dataset (train and validation) from either a provided path or by downloading it.
        If a dataset path is provided, it attempts to load from there. Otherwise, it downloads the dataset.

        :param data_set_path: Optional directory to load the dataset from.
        :return: A tuple of tuples containing (x_train, y_train) and (x_val, y_val).
        """
        # Download and extract annotations and images
        ann_file_train, ann_file_val = self._download_coco_data(data_set_path)
        self._download_coco_images(data_set_path)

        # Define transformations for the dataset
        transform = transforms.Compose([transforms.ToTensor()])

        # Load COCO dataset for training and validation
        train_data = CocoDetection(root=os.path.join(data_set_path, "train2017"),
                                   annFile=ann_file_train, transform=transform)
        val_data = CocoDetection(root=os.path.join(data_set_path, "val2017"),
                                 annFile=ann_file_val, transform=transform)

        # Create DataLoader
        train_loader = DataLoader(dataset=train_data, batch_size=64, shuffle=True, num_workers=2)
        val_loader = DataLoader(dataset=val_data, batch_size=64, shuffle=False, num_workers=2)

        # Prepare the data
        x_train, y_train = zip(*[batch for batch in train_loader])
        x_val, y_val = zip(*[batch for batch in val_loader])

        x_train = torch.cat(x_train)
        y_train = torch.cat(y_train)
        x_val = torch.cat(x_val)
        y_val = torch.cat(y_val)

        print(f"x_train shape: {x_train.shape}")
        print(f"y_train shape: {y_train.shape}")
        print(f"x_val shape: {x_val.shape}")
        print(f"y_val shape: {y_val.shape}")

        return (x_train, y_train), (x_val, y_val)

    def _download_coco_data(self, data_dir: str) -> Tuple[str, str]:
        """
        Downloads COCO dataset annotations if not already present.

        :param data_dir: The directory where the annotations are stored.
        :return: Paths to the COCO train and validation annotation files.
        """
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        ann_file_train = os.path.join(data_dir, "annotations", "instances_train2017.json")
        ann_file_val = os.path.join(data_dir, "annotations", "instances_val2017.json")

        if os.path.exists(ann_file_train) and os.path.exists(ann_file_val):
            print("COCO annotations already exist.")
            return ann_file_train, ann_file_val

        coco_annotations_url = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
        annotations_zip_file = os.path.join(data_dir, "annotations_trainval2017.zip")
        if not os.path.exists(annotations_zip_file):
            print("Downloading COCO annotations...")
            response = requests.get(coco_annotations_url)
            with open(annotations_zip_file, 'wb') as f:
                f.write(response.content)
            print("COCO annotations downloaded successfully!")

        try:
            print("Extracting annotations zip file...")
            with zipfile.ZipFile(annotations_zip_file, 'r') as zip_ref:
                zip_ref.extractall(data_dir)
            print("Annotations zip file extracted successfully!")
        except Exception as e:
            print("Error extracting annotations zip file:", e)

        return ann_file_train, ann_file_val

    def _download_coco_images(self, data_dir: str):
        """
        Downloads the COCO images for both training and validation sets if not already downloaded.

        :param data_dir: The directory where the images will be stored.
        """
        img_dir_train = os.path.join(data_dir, "train2017")
        img_dir_val = os.path.join(data_dir, "val2017")

        if os.path.exists(img_dir_train) and os.path.exists(img_dir_val):
            print("COCO images already exist.")
            return

        coco_images_url_train = "http://images.cocodataset.org/zips/train2017.zip"
        coco_images_url_val = "http://images.cocodataset.org/zips/val2017.zip"
        img_zip_file_train = os.path.join(data_dir, "train2017.zip")
        img_zip_file_val = os.path.join(data_dir, "val2017.zip")

        # Download and extract images for training set
        if not os.path.exists(img_zip_file_train):
            print("Downloading COCO images for training set...")
            response = requests.get(coco_images_url_train)
            with open(img_zip_file_train, 'wb') as f:
                f.write(response.content)
            print("COCO images for training set downloaded successfully!")
            print("Extracting images for training set...")
            with zipfile.ZipFile(img_zip_file_train, 'r') as zip_ref:
                zip_ref.extractall(data_dir)
            print("Images for training set extracted successfully!")

        # Download and extract images for validation set
        if not os.path.exists(img_zip_file_val):
            print("Downloading COCO images for validation set...")
            response = requests.get(coco_images_url_val)
            with open(img_zip_file_val, 'wb') as f:
                f.write(response.content)
            print("COCO images for validation set downloaded successfully!")
            print("Extracting images for validation set...")
            with zipfile.ZipFile(img_zip_file_val, 'r') as zip_ref:
                zip_ref.extractall(data_dir)
            print("Images for validation set extracted successfully!")