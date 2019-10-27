from collections import Callable


def bold(s: str, b: bool) -> str:
    return f"\033[1m{s}" if b else s


class Colors:
    yellow: Callable = lambda s, b=False: f"\033[93m{bold(s, b)}\033[0m"
    green: Callable = lambda s, b=False: f"\033[92m{bold(s, b)}\033[0m"
    gray: Callable = lambda s, b=False: f"\033[90m{bold(s, b)}\033[0m"
    blue: Callable = lambda s, b=False: f"\033[94m{bold(s, b)}\033[0m"
    red: Callable = lambda s, b=False: f"\033[91m{bold(s, b)}\033[0m"
