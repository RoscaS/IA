import time
from typing import Any, Dict

from graphs.SearchableGraph import SearchableGraph
from helpers.Colors import Colors


class AnimatedGraph(SearchableGraph):
    def __init__(self):
        super().__init__()
        self._refresh_delay = 0.3

    @property
    def refresh_delay(self) -> float:
        return self._refresh_delay

    @refresh_delay.setter
    def refresh_delay(self, value: float):
        self._refresh_delay = value

    def show_execution(self,
                       current: Any,
                       frontier: Any,
                       visited: Dict[Any, bool],
                       start: Any,
                       goal: Any = None) -> None:

        print("\n")
        time.sleep(self.refresh_delay)
        for c, v in enumerate(self.vertices):
            break_line = "\n" if c % self.width == 0 and c != 0 else ""
            vertex = v
            if v == current:
                vertex = Colors.green(v, True)
            elif v == goal:
                vertex = Colors.red('[GOALL]')
            elif v in frontier or v in [i[1] for i in frontier.elements]:
                vertex = Colors.blue(v, True)
            elif v in visited:
                if v == start:
                    vertex = Colors.green('[START]')
                else:
                    vertex = Colors.gray(v)

            print(f"{break_line}{vertex}", end="")
