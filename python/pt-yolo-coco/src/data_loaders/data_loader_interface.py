from abc import ABC, abstractmethod


class DataLoaderInterface(ABC):
    @abstractmethod
    def load(self, data_set_path: str):
        pass
