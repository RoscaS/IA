class Player:
    TOKENS = ["o", "x"]
    count = 0
    def __init__(self, name=None):
        Player.count += 1
        self.name = name if name is not None else f"Player {self.count}"
        self.token = Player.TOKENS[Player.count - 1]

    def __str__(self):
        return f"{self.name}: {self.token}"
