from abc import ABC, abstractmethod

from graphs import BaseGraph, Vertex


class SearchStrategy(ABC):

    def __str__(self) -> str:
        return self.__class__.__name__.replace("Strategy", "")

    @abstractmethod
    def search(self, graph: BaseGraph, start: Vertex, goal: Vertex): pass
