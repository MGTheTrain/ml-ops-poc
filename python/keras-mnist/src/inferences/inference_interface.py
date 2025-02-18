from abc import ABC, abstractmethod


class InferenceInterface(ABC):
    @abstractmethod
    def infer(self, model_path: str):
        pass
