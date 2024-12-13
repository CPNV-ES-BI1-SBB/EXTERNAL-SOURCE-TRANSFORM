from abc import ABC, abstractmethod

class CloudProvider(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def download(self, path: str) -> dict:
        pass

    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def _disconnect(self):
        pass