from GA.NumbersAndOperators import Gene


class GenePool:
    def __init__(self):
        self.pool = []

    def __str__(self):
       return "\n".join(str(i) for i in self.pool)

    def add(self, key, value):
        self.pool.append(Gene(key, value))

    def __contains__(self, item):
        return self.by_value(item) is not None

    def __getitem__(self, item):
        return self.by_value(item)


    def by_key(self, key):
        try:
            return list(filter(lambda x: x.key == key, self.pool))[0]
        except:
            return None

    def by_value(self, value):
        try:
            return list(filter(lambda x: x.value == value, self.pool))[0]
        except:
            return None

    def is_valid(self, value):
        return self.by_value(value) is not None
