import math

from graph.heuristics.HeuristicStrategy import HeuristicStrategy


class AsCrowFliesHeuristic(HeuristicStrategy):

    def compute(self, x1: int, y1: int, x2: int, y2: int) -> float:
        return math.sqrt((x2 - x1)**2 + (y2 - y1) ** 2)
