from TicTac.Grid import Grid
from TicTac.Player import Player


class Game:
    win = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    def __init__(self, player_a, player_b):
        self.pA = player_a
        self.pB = player_b
        self.grid = Grid(player_a, player_b)
        self.round = 0
        self.playing = player_a

    def __str__(self):
        tabs = lambda c: "\t" * c
        separator = tabs(4)
        names = f"\n{self.pA}{separator}{self.pB}"
        spacer = "" if self._is_pA() else tabs(6)
        underline = f"{spacer}{len(str(self.pA)) * '-'}"
        return f"\n{names}\n{underline}{self.grid}"

    def play(self):
        print(self)
        idx = self.getInput()
        self.grid.set(idx, self.playing)
        self.update()

    def update(self):
        self.playing = self.pB if self._is_pA() else self.pA
        self.round += 1

    def getInput(self):
        s = f"{self.playing.name}, what's your move: "
        move = input(s)
        s = "Invalid input! Try again: "
        while (not self._isValid(move)):
            move = input(s)
        return int(move) - 1

    def isWin(self):
        grid = self.grid
        for case in Game.win:
            if (grid[case[0]] != 0):
                if (grid[case[0]] == grid[case[1]]):
                    if (grid[case[0]] == grid[case[2]]):
                        return self.pA if grid[case[0]] == 1 else self.pB
        return None

    def start(self):
        winner = None
        while not winner:
            self.play()
            winner = self.isWin()
        print(self)
        print(f"{winner.name} win the game!")

    def _isValid(self, idx):
        try:
            cleaned = int(idx)
        except:
            return False
        if cleaned not in list(range(1, 10)):
            return False
        return self.grid[cleaned - 1] == 0

    def _is_pA(self):
        return self.playing is self.pA


game = Game(Player(), Player())
game.start()
