import heapq

class PriorityQueue:
    '''
    Simple wrapper around `heapq`
    '''
    def __init__(self):
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def push(self, item: object, priority: int):
        heapq.heappush(self, (priority, item))

    def pop(self) -> object:
        return heapq.heappop(self)[1]
