from abc import ABC, abstractmethod


class InferenceInterface(ABC):
    @abstractmethod
    def infer(self, model_path: str, image_path: str):
        pass
