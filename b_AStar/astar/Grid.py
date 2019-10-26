from dataclasses import dataclass

from graph.Graph import Graph


@dataclass(frozen=True)
class Point2D:
    x: int = 0
    y: int = 0

    def __repr__(self):
        return f"[{str(self.x).rjust(2)},{str(self.y).rjust(2)}]"


class Grid(Graph):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.build_graph()
        self.create_edges()

    def in_bounds(self, id):
        return 0 <= id.x < self.width and 0 <= id.y < self.height

    def build_graph(self):
        for y in range(self.height):
            for x in range(self.width):
                self.add_vertex(Point2D(x, y))

    def create_edges(self):
        for v in self.get_vertices():
            results = filter(self.in_bounds,
                             [Point2D(v.x + 1, v.y), Point2D(v.x, v.y - 1),
                              Point2D(v.x - 1, v.y), Point2D(v.x, v.y + 1)])
            for neighbor in results:
                self.add_edge(v, neighbor, 1)

    def show(self):
        for c, v in enumerate(self.vertices):
            break_line = "\n" if c % self.width == 0 and c != 0 else ""
            print(f"{break_line}{v}", end="")
