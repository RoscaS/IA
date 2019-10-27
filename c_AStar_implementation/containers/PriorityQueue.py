import heapq
from typing import Any, Iterator, Tuple, List


class PriorityQueue:
    '''
    Simple wrapper around `heapq`
    '''

    def __init__(self) -> None:
        self.elements: List[Tuple[float, Any]] = []

    def __contains__(self, item) -> bool:
        return item in self.elements

    def __iter__(self) -> Iterator:
        return iter(self.elements)

    def empty(self) -> bool:
        return not self.elements

    def add(self, item: Any, priority: int) -> None:
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Any:
        return heapq.heappop(self.elements)[1]
