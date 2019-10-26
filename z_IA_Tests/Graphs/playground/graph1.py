# https://graphviz.readthedocs.io/en/stable/examples.html#hello-py
from collections import deque

graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F', 'G'},
    'D': set(),
    'E': set(),
    'F': set(),
    'G': set(),
}

def depth_first_search(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            stack += (graph[vertex] - visited)
    return visited


def breadth_first(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex] - visited
    return visited



def best_first(graph, start, final):
    history = set()
    frontier = deque([start])
    while frontier:
        vertex = frontier.popleft()
        if vertex == final:
            return


if __name__ == '__main__':
    print(depth_first_search(graph, "A") == graph.keys())
    # print(breadth_first(graph, "A") == graph.keys())
