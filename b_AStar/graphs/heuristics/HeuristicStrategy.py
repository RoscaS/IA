from abc import ABC, abstractmethod


class HeuristicStrategy(ABC):

    def __str__(self) -> str:
        return self.__class__.__name__.replace("Heuristic", "")

    @abstractmethod
    def compute(self, x1: int, y1: int, x2: int, y2: int) -> int: pass
