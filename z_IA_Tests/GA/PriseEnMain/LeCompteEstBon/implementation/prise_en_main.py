from deap import base
from deap import creator
from deap import tools
from deap import algorithms
import operator
from enum import Enum
from collections import namedtuple
import random
import time

# Each operand or operator is described by 4 bits

CODE_LENGTH = 4

# In this example, we fix the number of operands to 5
NB_OPERANDS = 5

# The maximum number of operators is NB_OPERANDS - 1
# ex. 5 + 3 / 2
# three operands: 5, 3, 2
# two operators: +, /
NB_OPERATORS = NB_OPERANDS - 1

CHROMOSOME_LENGTH = NB_OPERANDS * CODE_LENGTH + NB_OPERATORS * CODE_LENGTH

# We have three types of code: operands, operators and undefined symbols
class CodeType(Enum):
    OPERAND = 1
    OPERATOR = 2
    NOTHING = 3

# namedtuple("typename, field_names[...]") returns a new tuple subclass named
# 'typename'.
# The new subclass is used to create tuple-like objects that have fields
# accessible
# by attribute lookup as well as being indexable and iterable
Code = namedtuple("Code", ["code_type", "apply", "str"])

# Standard operators as functions, see
# https://docs.python.org/3/library/operator.html
OPERATORS = {
    10: (operator.add, "+"),
    11: (operator.sub, "-"),
    12: (operator.mul, "*"),
    13: (operator.truediv, "/")
}

def _parse_code(code):
    """ Convert bit string to a Code namedtuple """
    int_value = int(code, 2)
    if int_value >= 0 and int_value < 10:
        return Code(CodeType.OPERAND, lambda: int_value, str(int_value))
    elif int_value >= 10 and int_value <= 13:
        return Code(CodeType.OPERATOR, OPERATORS[int_value][0],
                    OPERATORS[int_value][1])
    else:
        return Code(CodeType.NOTHING, None, "_")


# _=== No need to change something here. ===_
# You find here functions that may be interesting for you.

def _decode(individual):
    """ Parse each code of the full chromosome (aka individual) """
    chromosome_str = "".join([str(gene) for gene in individual])
    codes = [_parse_code(chromosome_str[i: i + CODE_LENGTH]) for i in
             range(0, len(chromosome_str), CODE_LENGTH)]
    return codes


def display_chromosome(individual):
    """ Convert chromosome to a readable format (e.g. 3 + 5 / 6) """
    return " ".join(code.str for code in _decode(individual))

def compute_chromosome(individual):
    """ Compute operations described by a the chromosome """
    codes = _decode(individual)
    first_operand = None
    operation = None
    snd_operand = None
    result = 0
    for code in codes:
        if not first_operand:
            if code.code_type == CodeType.OPERAND:
                first_operand = code.apply()
        elif not operation:
            if code.code_type == CodeType.OPERATOR:
                operation = code.apply
        elif not snd_operand:
            if code.code_type == CodeType.OPERAND:
                snd_operand = code.apply()
                try:
                    result = operation(first_operand, snd_operand)
                except ZeroDivisionError:
                    pass
                first_operand = result
                operation = None
                snd_operand = None
    return result


## Deap framework
# _=== No need to change something here. ===_
# You find here a preparation of tools necessary for our algorithm.

toolbox = base.Toolbox()

# The **fitness** will measure the proximity between the result of the chromosome and a target value.
# The **lower the proximity is - the better is our chromosome** so we are in a minimization problem.
# /!\ Be aware that `values` and `weights` must be tuples.

# First we create the code of our fitness function; then we add it into our toolbox.

def fitness(individual, target):
    return (abs(compute_chromosome(individual) - target),) # Tuple !

toolbox.register("fitness", fitness)

# The following line creates, in the `creator`, a ready to use single objective minimizing fitness named _FitnessMin_.
# `base.Fitness`: if values are provided as a tuple, the fitness is initalized using those values, otherwise it is empty (or invalid).
# `weights` is used to define a maximization/minimization by setting 1.0 or -1.0.

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))


# `deap.creator.create(name, base[, attribute[, ...]])`
# The `create()` function takes at least two arguments, a name for the newly created class and a base class. Any subsequent argument becomes an attribute of the class.


# A `deep.creator.Individual` will be list of gene with an attribute 'fitness' of type `deep.creator.FitnessMin` just created.
creator.create("Individual", list, fitness=creator.FitnessMin)

### TODO 1: OK
# Look at the documentation of the DEAP framework and register into the toolbox the following tools:
# - **Crossover** between two individuals will be a simple one point crossover.
# - **Mutation** of a individual will flip the bit in the gene with a probability of 10%.
# - **Selection** of *k* individuals will be done using *k* spins of a **tournament**.
# Then, complete the following cell:


toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# Finally we provide initiations operations. A **population** will be a list of `deep.creator.Individual`. Each gene will be set randomly to 0 or 1.

toolbox.register("init_gene", random.randint, 0, 1)
toolbox.register("init_individual", tools.initRepeat, creator.Individual, toolbox.init_gene, CHROMOSOME_LENGTH)
toolbox.register("init_population", tools.initRepeat, list, toolbox.init_individual)

## TODO 2: Solve "Le compte est bon"
# It'y sour turn! Using Deap and previous tools design a loop to obtain **TARGET** value in a maximum time of **MAX_TIME**.
# - Break the loop if an individual is optimal before **MAX_TIME** (i.e. his fitness = 0).
# - Display the best chromosome
# - Display the total time




class LeCompteEstBon:

    def __init__(self, target, time=5, pop=50, cxpb=.5, mutpb=.2, ngen=1000):
        self.max_time = time
        self.max_pop = pop
        self.target = target
        self.mutpb = mutpb
        self.cxpb = cxpb
        self.ngen = ngen

        self.generations = 0

        self.best = None
        self.duration = None

    def get_fitness(self, chromosome):
        score = toolbox.fitness(chromosome, self.target)
        chromosome.fitness.values = score
        if (self.best == None or score[0] < self.best.fitness.values[0]):
            self.best = chromosome
        return score[0]

    def apply_crossovers(self, offspring):
        for a, b in zip(offspring[::2], offspring[1::2]):
            if random.random() < self.cxpb:
                toolbox.mate(a, b)
                del a.fitness.values
                del b.fitness.values

    def apply_mutations(self, offspring):
        for chromosome in offspring:
            if random.random() < self.mutpb:
                toolbox.mutate(chromosome)
                del chromosome.fitness.values

    def run(self):
        start = time.time()

        population = toolbox.init_population(n=self.max_pop)

        while time.time() - start <= 5:

            for chromosome in population:
                score = self.get_fitness(chromosome)
                if (score == 0.0):
                    self.duration = time.time() - start
                    return self.best

            selection = toolbox.select(population, self.max_pop)
            offspring = [toolbox.clone(i) for i in selection]

            self.apply_crossovers(offspring)
            self.apply_mutations(offspring)

            population[:] = offspring
            self.generations += 1

        return self.best



TARGET = 126
MAX_TIME = 5  # seconds
CXPB, MUTPB, NGEN = 0.5, 0.2, 1000


x = LeCompteEstBon(TARGET)
result = x.run()
success = result.fitness.values[0] == 0.0

pretty = display_chromosome(result)
gens = f"Generations: {x.generations}"

print(f"\nTarget: {TARGET}")
if success:
    elapsed = "{:.2f}s".format(x.duration)
    print(f"{pretty}\nElapsed: {elapsed}\n{gens}")
else:
    score = x.best.fitness.values[0]
    timeout = f"Time out (> {MAX_TIME}s)\t\n"
    print(f"{timeout}Best value: {pretty}\nBest score: {score}\n{gens}")







# Some hints:
# - Take a look at Deap documentation https://deap.readthedocs.io/en/master/index.html
# - Create a small population `init_population(n)` and use `compute_chromosome(individual)`, `display_chromosome(individual)` and `individual.fitness` to clearly understand what is an Individual.
# Good luck!

## TODO 3: Advanced - Find the best Hyperparameters (optional)
# - Which are the **best**:
#     - population size
#     - frequence of mutation
#     - frequence of crossover
#     - ...
# - Implement the elitism, the best N individuals will surely survive (N = 2) and without undergoing mutation

