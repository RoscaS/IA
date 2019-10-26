from typing import Dict, KeysView, Any


class Vertex:
    def __init__(self, node: Any):
        self.id: Any = node
        self.adjacent: Dict[Vertex, int] = {}

    @property
    def connections(self) -> KeysView[Any]:
        return self.adjacent.keys()

    def __repr__(self):
        return f"Vertex<{type(self.id).__name__}>"

    def __str__(self):
        adjacent = '\n\t'.join(f"├{i.id}" for i in self.adjacent)
        return f"{self.id}\n\t{adjacent or None}"

    def add_neighbor(self, neighbor: Any, weight: int = 0):
        self.adjacent[neighbor] = weight

    def weight_to(self, neighbor: Any) -> int:
        return self.adjacent[neighbor]
