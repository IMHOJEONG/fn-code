from abc import ABC, abstractmethod

class PowerSource(ABC):
    def __init__(self, capacity: float):
        self._capacity = capacity;
        self._level = capacity;

    def level(self) -> float:
        return self._level
    
    @abstractmethod
    def consume(self, distance: float) -> float:
        pass

    