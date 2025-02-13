from abc import ABC, abstractmethod


class DataLoaderInterface(ABC):
    @abstractmethod
    def load(self):
        pass
