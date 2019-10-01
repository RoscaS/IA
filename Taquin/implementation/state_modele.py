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
    def get_x(values, x=0):
        for i, line in enumerate(values):
            for j, el in enumerate(line):
                if el == x:
                    return (i, j)

    def applicable_operators(self):
        ops = []
        rows = len(self.values)
        cols = len(self.values[0])

        i, j = self.get_x(self.values)
        push = lambda a, b: ops.append(self.swap(self.values, i, j, a, b))

        # swap with previous line
        if i > 0:
            push(i - 1, j)

        # swap with following line
        if i < rows - 1:
            push(i + 1, j)

        # swap with left side column
        if j > 0:
            push(i, j - 1)

        # swap with right side column
        if j < cols - 1:
            push(i, j + 1)

        return ops

    def apply(self, op):
        return State(op, self)
