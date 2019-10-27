import math
from typing import Any


class City:

    def __init__(self, name: str, x: str, y: str) -> None:
        self.name = name
        self.x = int(x)
        self.y = int(y)

    def __str__(self) -> str:
        return f"{self.name} ({self.x}; {self.y})"

    def __repr__(self) -> str:
        return f"{self.name} ({self.x}; {self.y})"

    def distance(self, other: Any) -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
