from collections import deque


class Queue:
    def __init__(self, elements=[]):
        self.elements = deque()
        for element in elements:
            self.put(element)

    def empty(self):
        return len(self.elements) == 0

    def put(self, element):
        self.elements.append(element)

    def get(self):
        return self.elements.popleft()
