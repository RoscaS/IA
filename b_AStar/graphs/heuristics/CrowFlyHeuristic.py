from graphs.heuristics.HeuristicStrategy import HeuristicStrategy


class CrowFlyHeuristic(HeuristicStrategy):

    def compute(self, x1: int, y1: int, x2: int, y2: int) -> float:
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        D1, D2 = 4, 1
        return D1 * max(dx, dy) + (D2 - D1) * min(dx, dy)
        # return math.sqrt((x1 - x2)**2 + (y1 - y2) ** 2)
