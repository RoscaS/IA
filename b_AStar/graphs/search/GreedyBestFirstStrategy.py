
from graphs import Vertex, BaseGraph
from graphs.search.SearchStrategy import SearchStrategy
from helpers.PriorityQueue import PriorityQueue


class GreedyBestFirstStrategy(SearchStrategy):

    def search(self, graph: BaseGraph, start: Vertex, goal: Vertex) -> None:
        frontier = PriorityQueue()
        frontier.add(start.id, 0)
        path = {start.id: None}

        while not frontier.empty():
            current = frontier.get()

            if current == goal.id:
                break

            for next in graph.get_vertex(current).connections:
                if next.id not in path:

                    x1, y1 = next.id.x, next.id.y
                    x2, y2 = goal.id.x, goal.id.y

                    priority = graph.heuristic.compute(x1, y1, x2, y2)

                    frontier.add(next.id, priority)
                    path[next.id] = current

                    graph.show_execution(current, frontier, path, start.id, goal.id)
