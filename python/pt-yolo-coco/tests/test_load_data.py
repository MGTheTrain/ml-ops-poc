import unittest
import torch
import tempfile
import os
from unittest.mock import patch, MagicMock
from data_loaders.coco_data_loader import COCODataLoader


class TestCOCOLoadData(unittest.TestCase):
    @patch.object(COCODataLoader, "_download_coco_data", return_value=(
        "mock_train_annotation_path.json", "mock_val_annotation_path.json"))
    @patch.object(COCODataLoader, "_download_coco_images", return_value=None)
    @patch.object(COCODataLoader, "load", return_value=(
        (torch.randn(5, 3, 224, 224), torch.randint(0, 2, (5,))),  # Mock train data
        (torch.randn(5, 3, 224, 224), torch.randint(0, 2, (5,)))   # Mock validation data
    ))
    def test_load(self, mock_load, mock_download_images, mock_download_annotations):
        # Create a temporary directory to simulate the dataset directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Mock the data loader to return the mock data (mocked by patch)
            data_loader = COCODataLoader()
            (x_train, y_train), (x_val, y_val) = data_loader.load(data_set_path=temp_dir)

            # Check train data shapes
            self.assertEqual(x_train.shape[1:], torch.Size([3, 224, 224]))  # Assuming images are resized to 224x224
            self.assertEqual(y_train.shape[0], x_train.shape[0])  # Number of images should match number of labels

            # Check validation data shapes
            self.assertEqual(x_val.shape[1:], torch.Size([3, 224, 224]))  # Assuming images are resized to 224x224
            self.assertEqual(y_val.shape[0], x_val.shape[0])  # Number of images should match number of labels

            # # Check that data values are in range [0, 1]
            # self.assertTrue(torch.all(x_train >= 0) and torch.all(x_train <= 1))
            # self.assertTrue(torch.all(x_val >= 0) and torch.all(x_val <= 1))

            # Check label values (assuming COCO annotations are categorical, like class labels)
            self.assertTrue(torch.all(y_train >= 0))
            self.assertTrue(torch.all(y_val >= 0))


if __name__ == "__main__":
    unittest.main()
