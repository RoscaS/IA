from graph.Graph import Graph
from graph.Vertex import Vertex
from graph.heuristics import HeuristicStrategy
from graph.heuristics.AsCrowFliesHeuristic import AsCrowFliesHeuristic
from graph.heuristics.ManhatanHeuristic import ManhatanHeuristic
from graph.heuristics.NullHeuristic import NullHeuristic
from graph.heuristics.XHeuristic import XHeuristic
from graph.heuristics.YHeuristic import YHeuristic
from graph.search import SearchStrategy
from graph.search.AStartStrategy import AStarStrategy


class SearchableGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self._strategy: SearchStrategy = AStarStrategy()
        self._heuristic: HeuristicStrategy = ManhatanHeuristic()

    @property
    def strategy(self) -> SearchStrategy:
        return self._strategy

    @property
    def heuristic(self) -> HeuristicStrategy:
        return self._heuristic

    @strategy.setter
    def strategy(self, strategy: SearchStrategy) -> None:
        self._strategy = strategy

    @heuristic.setter
    def heuristic(self, heuristic: HeuristicStrategy) -> None:
        self._heuristic = heuristic

    def set_AStartStrategy(self) -> None:
        self.strategy = AStarStrategy()

    def set_NullHeuristic(self) -> None:
        self.heuristic = NullHeuristic()

    def set_XHeuristic(self) -> None:
        self.heuristic = XHeuristic()

    def set_YHeuristic(self) -> None:
        self.heuristic = YHeuristic()

    def set_ManhatanHeuristic(self) -> None:
        self.heuristic = ManhatanHeuristic()

    def set_AsCrowFliesHeuristic(self) -> None:
        self.heuristic = AsCrowFliesHeuristic()

    def search(self, start: Vertex, goal: Vertex):
        print(f"\n\nStarting search with {self.strategy} + {self.heuristic}")
        print(f"from {start.id} to {goal.id}\n")
        return self.strategy.search(self, start, goal)
