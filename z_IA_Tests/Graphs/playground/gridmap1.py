import os
import time
from collections import deque

width = 20
height = 10

class Node:
    def __init__(self, x, y):
        self.visited = False
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str([self.x, self.y])

    def __repr__(self):
        return str([self.x, self.y])

    def __hash__(self):
        return str(self).__hash__()

    @property
    def state(self):
        return " o " if self.visited else " . "

class Graph:
    def __init__(self, width, height):
        self.nodes = []
        for x in range(height):
            for y in range(width):
                self.nodes.append(Node(y, x))

    def __str__(self):
        s = ""
        for c, node in enumerate(self.nodes):
            s += node.state
            s += "" if node.x != width -1 else "\n"
        return s

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def get_node(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node

    def neighbors(self, node):
        directions = [Node(1, 0), Node(0, 1), Node(-1, 0), Node(0, -1)]
        result = []
        for dir in directions:
            neighbor = self.get_node(node.x + dir.x, node.y + dir.y)
            if neighbor in self.nodes:
                result.append(neighbor)
        return result


if __name__ == '__main__':
    graph = Graph(20, 10)
    start = graph.nodes[109]
    # graph.nodes[109].visited = True
    # print(graph)
    breadth_first(graph, start)


