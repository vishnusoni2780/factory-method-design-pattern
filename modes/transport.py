from abc import ABC, abstractmethod

# Interface Class
class Transport(ABC):
    @abstractmethod
    def run(self):
        pass
