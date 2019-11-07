from dataclasses import dataclass, field


class Gene:

    def __init__(self, key, value):
        self.key = key
        self.value = "{:04b}".format(value)

    def __str__(self):
        return f"{self.key}: {self.value}"

    def __repr__(self):
        return self.__str__()



