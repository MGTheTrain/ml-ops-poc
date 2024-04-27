import os
import requests
import zipfile
from pycocotools.coco import COCO
from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision.datasets import CocoDetection

def download_coco_data(data_dir):
    # Create directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Define path to COCO annotations file
    ann_file_train = os.path.join(data_dir, "annotations", "instances_train2017.json")
    ann_file_val = os.path.join(data_dir, "annotations", "instances_val2017.json")

    # Check if the annotations file exists
    if os.path.exists(ann_file_train) and os.path.exists(ann_file_val):
        print("COCO annotations already exist.")
        return ann_file_train, ann_file_val

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

    # Extract the annotations zip file
    try:
        print("Extracting annotations zip file...")
        with zipfile.ZipFile(annotations_zip_file, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print("Annotations zip file extracted successfully!")
    except Exception as e:
        print("Error extracting annotations zip file:", e)

    return ann_file_train, ann_file_val

def download_coco_images(data_dir):
    # Define path to COCO images directory
    img_dir_train = os.path.join(data_dir, "train2017")
    img_dir_val = os.path.join(data_dir, "val2017")

    # Check if the images directory already exists
    if os.path.exists(img_dir_train) and os.path.exists(img_dir_val):
        print("COCO images already exist.")
        return

    # Download the COCO dataset images. NOTE: Tens of thousands of images ->  
    # - Storage: The COCO dataset, along with model checkpoints and training logs, can occupy a substantial amount of disk space. Fast storage, such as SSDs, is preferred for quick access to data during training.
    # - GPU: Deep learning models, especially large ones like YOLOv4, benefit greatly from parallel processing units like GPUs. High-end GPUs from NVIDIA such as the GeForce RTX series or Tesla GPUs are commonly used for training deep learning models due to their high computational power and support for frameworks like TensorFlow and PyTorch.
    # - Memory: Large datasets like COCO may require a significant amount of memory (both GPU memory and system memory) to load and process efficiently during training. Having ample GPU memory ensures that the entire dataset and model can be loaded into memory, reducing the need for frequent data transfers between the GPU and system memory.
    # - CPU: While most of the computation is offloaded to the GPU during training, a powerful CPU is still important for tasks like data preprocessing, model initialization, and managing the training process.
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

def load_dataset(batch_size=64, train=True, data_dir='./data'):
    # Download COCO dataset annotations if not already downloaded
    ann_file_train, ann_file_val = download_coco_data(data_dir)

    # Download COCO dataset images if not already downloaded
    download_coco_images(data_dir)

    # Define transformations for the dataset
    transform = transforms.Compose([
        transforms.ToTensor(),  # Convert image to PyTorch tensor
    ])

    # Specify the path to the COCO dataset images
    img_folder = 'train2017' if train else 'val2017'

    # Load the COCO dataset using CocoDetection
    coco_dataset = CocoDetection(root=os.path.join(data_dir, img_folder), annFile=ann_file_train if train else ann_file_val, transform=transform)

    # Create a DataLoader to iterate through the dataset in batches
    data_loader = DataLoader(dataset=coco_dataset, batch_size=batch_size, shuffle=True, num_workers=2)

    return data_loader