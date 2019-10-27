from Graphs.redblob.GridWithWeights import GridWithWeights
from Graphs.redblob.SquareGrid import SquareGrid
from Graphs.redblob.helpers import DIAGRAM1_WALLS, \
    DIAGRAM4_WALLS, \
    DIAGRAM4_WEIGHTS
from Graphs.redblob.search import *


def breadth_first():
    grid = SquareGrid(30, 15)
    grid.walls = DIAGRAM1_WALLS
    start, goal = (8, 7), (17, 2)
    breadth_first_search_3(grid, start, goal, grid)


def dijkstra():
    grid = GridWithWeights(10, 10)
    grid.walls = DIAGRAM4_WALLS
    grid.weights = DIAGRAM4_WEIGHTS
    start, goal = (1, 4), (7, 8)

    came_from, cost_so_far = dijkstra_search(grid, start=start, goal=goal)
    draw_grid(grid, width=3, point_to=came_from, start=start, goal=goal)
    draw_grid(grid, width=3, number=cost_so_far, start=start, goal=goal)
    draw_grid(grid, width=3,
              path=reconstruct_path(came_from, start=start, goal=goal))


def greedy_best_first():
    grid = GridWithWeights(10, 10)
    start, goal = (0, 2), (7, 8)
    came_from = greedy_best_first_search(grid, start, goal)
    draw_grid(grid, width=3, point_to=came_from, start=start, goal=goal)
    draw_grid(grid, width=3,
              path=reconstruct_path(came_from, start=start, goal=goal))


def a_star():
    grid = GridWithWeights(10, 10)
    # grid.walls = DIAGRAM4_WALLS
    # grid.weights = DIAGRAM4_WEIGHTS
    start, goal = (1, 4), (7, 8)

    came_from, cost_so_far = a_star_search(grid, start=start, goal=goal)
    draw_grid(grid, width=3, point_to=came_from, start=start, goal=goal)
    draw_grid(grid, width=3, number=cost_so_far, start=start, goal=goal)
    draw_grid(grid, width=3,
              path=reconstruct_path(came_from, start=start, goal=goal))

    for k, v in came_from.items():
        print(f"{k}: {v}")


if __name__ == '__main__':
    # breadth_first()
    # dijkstra()
    # greedy_best_first()
    a_star()
