from abc import ABC, abstractmethod


class TrainingInterface(ABC):
    @abstractmethod
    def train(self):
        pass
