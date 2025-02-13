from abc import ABC, abstractmethod


class ModelInterface(ABC):
    @abstractmethod
    def build(self):
        pass
