from abc import ABC, abstractmethod


class TrainingInterface(ABC):
    @abstractmethod
    def train(self, model_path: str, data_set_path: str):
        pass
