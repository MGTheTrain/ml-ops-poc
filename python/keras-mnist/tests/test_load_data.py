import unittest
from data_loaders.mnist_data_loader import MNISTDataLoader


class TestLoadData(unittest.TestCase):
    def test_load(self):
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load()

        # Check data shapes
        self.assertEqual(x_train.shape, (60000, 28, 28, 1))
        self.assertEqual(y_train.shape, (60000,))
        self.assertEqual(x_test.shape, (10000, 28, 28, 1))
        self.assertEqual(y_test.shape, (10000,))

        # Check data normalization
        self.assertTrue((x_train >= 0).all() and (x_train <= 1).all())
        self.assertTrue((x_test >= 0).all() and (x_test <= 1).all())


if __name__ == "__main__":
    unittest.main()
