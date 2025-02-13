from abc import ABC, abstractmethod


class InferenceInterface(ABC):
    @abstractmethod
    def infer(self):
        pass
