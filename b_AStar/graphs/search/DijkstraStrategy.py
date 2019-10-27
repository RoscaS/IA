from graphs import Vertex, BaseGraph
from graphs.search.SearchStrategy import SearchStrategy
from helpers.PriorityQueue import PriorityQueue


class DijkstraStrategy(SearchStrategy):

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
                    priority = new_cost
                    frontier.add(next.id, priority)
                    path[next.id] = current

                    graph.show_execution(current, frontier, path, start.id, goal.id)
