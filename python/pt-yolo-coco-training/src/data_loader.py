import os
import requests
import zipfile
from pycocotools.coco import COCO
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import CocoDetection

def download_coco_data(data_dir):
    # Create directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Define path to COCO annotations file
    ann_file_train = os.path.join(data_dir, "annotations", "instances_train2017.json")
    ann_file_val = os.path.join(data_dir, "annotations", "instances_val2017.json")

    # Download the COCO dataset annotations
    coco_annotations_url = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
    annotations_zip_file = os.path.join(data_dir, "annotations_trainval2017.zip")
    if not os.path.exists(annotations_zip_file):
        print("Downloading COCO annotations...")
        response = requests.get(coco_annotations_url)
        with open(annotations_zip_file, 'wb') as f:
            f.write(response.content)
        print("COCO annotations downloaded successfully!")
    else:
        print("COCO annotations zip file already exists")
        return ann_file_train, ann_file_val

    # Check if the file exists after downloading.
    if os.path.exists(annotations_zip_file):
        print("Annotations zip file exists:", annotations_zip_file)
        
        # Extract the annotations zip file
        try:
            print("Extracting annotations zip file...")
            with zipfile.ZipFile(annotations_zip_file, 'r') as zip_ref:
                zip_ref.extractall(data_dir)
            print("Annotations zip file extracted successfully!")
        except Exception as e:
            print("Error extracting annotations zip file:", e)
    else:
        print("Annotations zip file does not exist:", annotations_zip_file)

    return ann_file_train, ann_file_val


def load_dataset(batch_size=64, train=True, data_dir='./data'):
    # Download COCO dataset annotations if not already downloaded
    ann_file_train, ann_file_val = download_coco_data(data_dir)

    # Define transformations for the dataset
    transform = transforms.Compose([
        transforms.Resize((416, 416)),  # Resize image to 416x416
        transforms.ToTensor(),           # Convert image to PyTorch tensor
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize image
    ])

    # Specify the path to the COCO dataset images
    img_folder = 'instances_train2017.json' if train else 'instances_val2017.json'

    # Load the COCO dataset using CocoDetection
    coco_dataset = CocoDetection(root=os.path.join(data_dir, img_folder), annFile=ann_file_train if train else ann_file_val, transform=transform)

    # Create a DataLoader to iterate through the dataset in batches
    data_loader = DataLoader(dataset=coco_dataset, batch_size=batch_size, shuffle=True, num_workers=2)

    return data_loader