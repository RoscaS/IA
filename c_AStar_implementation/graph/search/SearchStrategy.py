from abc import ABC, abstractmethod

from graph.Graph import Graph
from graph.Vertex import Vertex


class SearchStrategy(ABC):

    def __str__(self) -> str:
        return self.__class__.__name__.replace("Strategy", "")

    @abstractmethod
    def search(self, graph: Graph, start: Vertex, goal: Vertex): pass
