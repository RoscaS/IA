from graphs.Grid import Grid
from helpers.Point2D import Point2D

g = Grid(20, 10)
g.refresh_delay = 0.1
g.set_AStartStrategy()
g.set_CrowFlyHeuristic()

# start = Vertex(Point2D(10, 5))
# goal = Vertex(Point2D(18, 6))

goal = g.get_vertex(Point2D(4, 1))
start = g.get_vertex(Point2D(18, 8))



g.search(start, goal)

