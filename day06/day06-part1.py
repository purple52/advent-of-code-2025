from collections import namedtuple
from functools import reduce
from operator import add, mul

OPERATORS = { "+": add, "*": mul }
Problem = namedtuple("Problem", 'numbers operator')

def to_problem(strings):
    return Problem(map(int, strings[:-1]), OPERATORS[strings[-1]])

def calculate(problem):
    return reduce(problem.operator, problem.numbers)

def grand_total():
    data = [l.split() for l in open('input/actual.txt').read().splitlines()]
    return sum(map(calculate, map(to_problem, zip(*data))))

print(grand_total())