from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Point2D:
    x: int = 0
    y: int = 0

    def __repr__(self) -> str:
        return f"[{str(self.x).rjust(2)},{str(self.y).rjust(2)}]"
