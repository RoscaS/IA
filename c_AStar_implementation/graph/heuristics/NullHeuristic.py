from graph.heuristics.HeuristicStrategy import HeuristicStrategy


class NullHeuristic(HeuristicStrategy):

    def compute(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return 0
