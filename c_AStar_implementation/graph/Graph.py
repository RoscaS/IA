from typing import Dict, KeysView, Any, Iterator

from graph.Vertex import Vertex


class Graph:
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

    def add_edge(self, src: Any, dst: Any, weight=0) -> None:
        for element in [src, dst]:
            if element not in self.vertices:
                self.add_vertex(element)

        self.vertices[src].add_neighbor(self.vertices[dst], int(weight))
        self.vertices[dst].add_neighbor(self.vertices[src], int(weight))

    def get_vertices(self) -> KeysView[Any]:
        return self.vertices.keys()
