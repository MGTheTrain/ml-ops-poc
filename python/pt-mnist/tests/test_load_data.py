import unittest
import torch
from src.data_loaders.mnist_data_loader import MNISTDataLoader


class TestLoadData(unittest.TestCase):
    def test_load(self):
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load()

        # Check data shapes
        self.assertEqual(x_train.shape, torch.Size([60000, 1, 28, 28]))
        self.assertEqual(y_train.shape, torch.Size([60000]))
        self.assertEqual(x_test.shape, torch.Size([10000, 1, 28, 28]))
        self.assertEqual(y_test.shape, torch.Size([10000]))

        # Check data normalization
        self.assertTrue(torch.all(x_train >= -1) and torch.all(x_train <= 1))
        self.assertTrue(torch.all(x_test >= -1) and torch.all(x_test <= 1))


if __name__ == "__main__":
    unittest.main()
