from collections import deque


def create_grid(width, height):
    nodes = []
    for x in range(width):
        for y in range(height):
            nodes.append([x, y])
    return nodes


def neighbors(node, grid):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for direction in directions:
        neighbor = [node[0] + direction[0], node[1] + direction[1]]
        if neighbor in grid:
            result.append(neighbor)
    return result


def breath_first(start, grid):
    frontier = deque([start])
    visited = {start: True}

    while frontier:
        current = frontier.popleft()
        print(current)
        for next in neighbors(grid, current):
            if next not in visited:
                frontier.append(next)
                visited[next] = True


map = create_grid(20, 10)
# breath_first(map[0], map)

d = {[1,2,3]: "yes"}



