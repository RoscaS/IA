from collections import deque

from graphs import BaseGraph, Vertex
from graphs.search.SearchStrategy import SearchStrategy


class BreathFirstStrategy(SearchStrategy):

    def search(self, graph: BaseGraph, start: Vertex, goal: Vertex) -> None:
        frontier = deque([start.id])
        visited = {start.id: True}

        while not len(frontier) == 0:
            current = frontier.popleft()
            for next in graph.get_vertex(current).connections:
                if next.id not in visited:
                    frontier.append(next.id)
                    visited[next.id] = True

                    graph.show_execution(current, frontier, visited, start)

        assert len(visited) == graph.width * graph.height
