from graphs import Vertex
from graphs.BaseGraph import BaseGraph
from graphs.heuristics import HeuristicStrategy
from graphs.heuristics.CrowFlyHeuristic import CrowFlyHeuristic
from graphs.heuristics.ManhatanHeuristic import ManhatanHeuristic
from graphs.search import SearchStrategy
from graphs.search.AStartStrategy import AStarStrategy

from graphs.search.BreathFirstStrategy import BreathFirstStrategy
from graphs.search.DijkstraStrategy import DijkstraStrategy
from graphs.search.GreedyBestFirstStrategy import GreedyBestFirstStrategy


class SearchableGraph(BaseGraph):
    def __init__(self) -> None:
        super().__init__()
        self._strategy: SearchStrategy = BreathFirstStrategy()
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

    def set_BreathFirstStrategy(self) -> None:
        self.strategy = BreathFirstStrategy()

    def set_DijkstraStrategy(self) -> None:
        self.strategy = DijkstraStrategy()

    def set_GreedyBestFirstStrategy(self) -> None:
        self.strategy = GreedyBestFirstStrategy()

    def set_AStartStrategy(self) -> None:
        self.strategy = AStarStrategy()

    def set_ManhatanHeuristic(self) -> None:
        self.heuristic = ManhatanHeuristic()

    def set_CrowFlyHeuristic(self) -> None:
        self.heuristic = CrowFlyHeuristic()

    def search(self, start: Vertex, goal: Vertex):
        print(f"Starting search with {self.strategy} + {self.heuristic}")
        print(f"{start.id}\t{goal.id}")
        return self.strategy.search(self, start, goal)
