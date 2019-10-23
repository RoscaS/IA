class Grid:

    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b
        self.grid = [0 for i in range(9)]
        self.tokens = [" ", player_a.token, player_b.token]

    def __str__(self):
        values = [self.tokens[i] for i in self.grid]
        return """
             {} | {} | {}
            ---+---+---
             {} | {} | {}
            ---+---+---
             {} | {} | {}
            """.format(*values)

    def __getitem__(self, idx):
        return self.grid[idx]

    def __setitem__(self, idx, value):
        self.grid[idx] = value

    def set(self, idx, player):
        self.grid[idx] = self.tokens.index(player.token)




