from collections import deque

from astar.Grid import Grid, Point2D
from graph.Graph import Graph



g = Grid(20, 10)

# g.show()



def breath_first(graph, start):
    frontier = deque([start])
    visited = {start: True}

    while not len(frontier) == 0:
        current = frontier.popleft()
        print(f"Visiting: {current}")
        for next in graph.get_vertex(current).connections:
            if next.id not in visited:
                frontier.append(next.id)
                visited[next.id] = True

    print(len(visited))




breath_first(g, Point2D(10, 5))


