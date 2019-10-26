from copy import deepcopy


class State(object):

    def __init__(self, values, parent=None):
        self.values = values
        self.parent = parent

    def legal(self):
        pass

    def final(self, final_values):
        return self.values == final_values

    def __hash__(self):
        return str(self).__hash__()

    def __str__(self):
        return str(self.values)

    def __eq__(self, other):
        return self.values == other.values

    @staticmethod
    def swap(values, x1, y1, x2, y2):
        new = deepcopy(values)
        new[x1][y1], new[x2][y2] = new[x2][y2], new[x1][y1]
        return new

    @staticmethod
    def get_position(values):
        for x, line in enumerate(values):
            for y, el in enumerate(line):
                if el == 0:
                    return (x, y)

    def applicable_operators(self):
        ops = []
        rows = len(self.values)
        cols = len(self.values[0])

        x, y = self.get_position(self.values)
        push = lambda a, b: ops.append(self.swap(self.values, x, y, a, b))

        # swap with previous line
        if x > 0:
            push(x - 1, y)

        # swap with following line
        if x < rows - 1:
            push(x + 1, y)

        # swap with left side column
        if y > 0:
            push(x, y - 1)

        # swap with right side column
        if y < cols - 1:
            push(x, y + 1)

        return ops

    def apply(self, op):
        return State(op, self)
