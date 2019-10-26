from Graphs.redblob.PriorityQueue import PriorityQueue
from Graphs.redblob.Queue import Queue
from Graphs.redblob.helpers import draw_grid
from Graphs.redblob.heuristics import manhatan_tie_breaker


def breadth_first_search_1(graph, start):
    frontier = Queue([start])
    visited = {start: True}

    while not frontier.empty():
        current = frontier.get()
        print(f"Visiting {current}")
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True


def breadth_first_search_2(graph, start, grid):
    frontier = Queue([start])
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()

        draw_grid(grid, point_to=came_from, start=start)

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from


def breadth_first_search_3(graph, start, goal, grid):
    frontier = Queue([start])
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()

        draw_grid(grid, point_to=came_from, start=start, goal=goal)

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from


def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(next)
            if new_cost < cost_so_far.get(next, 99999):
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def greedy_best_first_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()
        # draw_grid(graph, width=3, point_to=came_from, start=start, goal=goal)

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                priority = manhatan_tie_breaker(goal, next, start)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(next)

            if new_cost < cost_so_far.get(next, 99999):
            # if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + manhatan_tie_breaker(goal, next, start)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far



def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
