from data_loaders.mnist_data_loader import MNISTDataLoader
from models.simple_nn import SimpleNN
from training.training_interface import TrainingInterface


class MNISTTraining(TrainingInterface):
    def train(
        self, model_path: str = "../models/mnist_model.h5", data_set_path: str = ""
    ) -> None:
        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load(
            data_set_path=data_set_path
        )

        simple_nn = SimpleNN()
        model = simple_nn.build()

        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )

        model.fit(x_train, y_train, epochs=10, batch_size=32)
        model.save(model_path)
