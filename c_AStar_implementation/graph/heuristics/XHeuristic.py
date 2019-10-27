from graph.heuristics.HeuristicStrategy import HeuristicStrategy


class XHeuristic(HeuristicStrategy):

    def compute(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2)
