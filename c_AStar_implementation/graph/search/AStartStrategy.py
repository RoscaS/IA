import time

from graph import Vertex, SearchableGraph
from graph.search.SearchStrategy import SearchStrategy
from containers.PriorityQueue import PriorityQueue


class AStarStrategy(SearchStrategy):

    def search(self,
               graph: SearchableGraph,
               start: Vertex,
               goal: Vertex) -> Vertex or None:

        frontier = PriorityQueue()
        frontier.add(start, 0)
        cost_so_far = {start: 0}
        counter = 0

        while not frontier.empty():
            current = frontier.get()
            counter += 1

            if current == goal:
                return (current, counter)

            for next in current.connections:
                new_cost = cost_so_far[current] + current.weight_to(next)

                if new_cost < cost_so_far.get(next, 99999):
                    cost_so_far[next] = new_cost

                    x1, y1 = next.id.x, next.id.y
                    x2, y2 = goal.id.x, goal.id.y

                    heuristic = graph.heuristic.compute(x2, y2, x1, y1)
                    priority = new_cost + heuristic

                    next.parent = current
                    frontier.add(next, priority)

        return None
