from collections import namedtuple
from functools import reduce
from itertools import groupby
from operator import add, mul

OPERATORS = { "+": add, "*": mul }
Problem = namedtuple("Problem", 'numbers operator')


def to_problem(data):
    to_number = lambda l: int(''.join(l[:-1]).strip())
    return Problem(map(to_number, data), OPERATORS[data[0][-1]])

def split_into_problems(input_data):
    is_delimiter = lambda s: all(c == ' ' for c in s)
    return map(to_problem, (list(g) for is_delim, g in groupby(input_data, is_delimiter) if not is_delim))

def calculate(problem):
    return reduce(problem.operator, problem.numbers)

def grand_total():
    lines = open('input/actual.txt').read().splitlines()
    return sum(map(calculate, split_into_problems(zip(*lines))))

print(grand_total())