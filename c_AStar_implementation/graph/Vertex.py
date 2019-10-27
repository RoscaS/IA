from typing import Dict, KeysView, Any, List


class Vertex:

    def __init__(self, node: Any) -> None:
        self.id: Any = node
        self.adjacent: Dict[Vertex, int] = {}
        self.parent: Vertex = None

    @property
    def connections(self) -> KeysView[Any]:
        return self.adjacent.keys()

    def __repr__(self) -> str:
        return f"Vertex<{type(self.id).__name__}>"

    def __str__(self) -> str:
        format = lambda w, id: f"├─{w}→{id}"
        string = '\n\t'.join(format(v, k.id) for k, v in self.adjacent.items())
        return f"\n{self.id}\n\t{string or None}"

    def __lt__(self, other):
        pass

    def add_neighbor(self, neighbor: Any, weight: int = 0) -> None:
        self.adjacent[neighbor] = weight

    def weight_to(self, neighbor: Any) -> int:
        return self.adjacent[neighbor]

    def get_path(self, start: Any) -> List[Any]:
        path = [self]
        pointer = self.parent
        while pointer.parent is not None:
            path.append(pointer)
            pointer = pointer.parent
        path.append(start)
        return list(reversed(path))
