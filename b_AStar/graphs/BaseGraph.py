from typing import Dict, KeysView, Any, Iterator

from graphs.Vertex import Vertex


class BaseGraph:
    def __init__(self) -> None:
        self.vertices: Dict[Any, Vertex] = {}

    def __iter__(self) -> Iterator[Vertex]:
        return iter(self.vertices.values())

    def add_vertex(self, node: Any) -> Vertex:
        vertex = Vertex(node)
        self.vertices[node] = vertex
        return vertex

    def get_vertex(self, node: Any) -> Vertex or None:
        return self.vertices.get(node, None)

    def add_edge(self, source: Any, destination: Any, weight=0) -> None:
        for element in [source, destination]:
            if element not in self.vertices:
                self.add_vertex(element)

        self.vertices[source].add_neighbor(self.vertices[destination], weight)
        self.vertices[destination].add_neighbor(self.vertices[source], weight)

    def get_vertices(self) -> KeysView[Any]:
        return self.vertices.keys()
