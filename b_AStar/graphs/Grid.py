from graphs.AnimatedGraph import AnimatedGraph
from helpers.Point2D import Point2D


class Grid(AnimatedGraph):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.width: int = width
        self.height: int = height
        self._build_graph()
        self._create_edges()

    def _in_bounds(self, id) -> bool:
        return 0 <= id.x < self.width and 0 <= id.y < self.height

    def _build_graph(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                self.add_vertex(Point2D(x, y))

    def _create_edges(self) -> None:
        for v in self.get_vertices():
            results = [Point2D(v.x + 1, v.y), Point2D(v.x, v.y - 1),
                       Point2D(v.x - 1, v.y), Point2D(v.x, v.y + 1)]

            results = filter(self._in_bounds, results)
            for neighbor in results:
                self.add_edge(v, neighbor, 1)


