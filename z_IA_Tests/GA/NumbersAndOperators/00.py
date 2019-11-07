import random

from GA.NumbersAndOperators import GenePool

b = lambda x: "{:04b}".format(x)

s = 23
f = lambda x: 1 / (s - x)
m = lambda: random.randint(1, 1000) == 0  # mutation rate
x = lambda: random.randint(1, 10) <= 7  # cross rate
pop_count = 50
max_generations = 1000
genes_per_chromosom = 8


pool = GenePool()

def encode_genes():
    for i in range(10):
        pool.add(str(i), i)
    pool.add("+", 0b_1010)
    pool.add("-", 0b_1011)
    pool.add("*", 0b_1100)
    pool.add("/", 0b_1101)

encode_genes()





