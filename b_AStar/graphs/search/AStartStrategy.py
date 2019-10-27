from graphs import Vertex, BaseGraph
from graphs.search.SearchStrategy import SearchStrategy
from helpers.PriorityQueue import PriorityQueue


class AStarStrategy(SearchStrategy):

    def search(self, graph: BaseGraph, start: Vertex, goal: Vertex) -> None:
        frontier = PriorityQueue()
        frontier.add(start.id, 0)
        path = {start.id: None}
        cost_so_far = {start: 0}

        while not frontier.empty():
            current = frontier.get()

            if current == goal.id:
                break

            vertex = graph.get_vertex(current)

            for next in vertex.connections:
                new_cost = cost_so_far[vertex] + vertex.weight_to(next)

                if new_cost < cost_so_far.get(next, 99999):
                    cost_so_far[next] = new_cost

                    x1, y1 = next.id.x, next.id.y
                    x2, y2 = goal.id.x, goal.id.y

                    heuristic = graph.heuristic.compute(x2, y2, x1, y1)
                    priority = new_cost + heuristic

                    print(f"\ng: {new_cost}\th: {heuristic}\tf: {priority}")

                    frontier.add(next.id, priority)
                    path[next.id] = current

                    graph.show_execution(current, frontier, path, start.id, goal.id)

