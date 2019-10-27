from graph.heuristics.HeuristicStrategy import HeuristicStrategy


class YHeuristic(HeuristicStrategy):

    def compute(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(y1 - y2)

