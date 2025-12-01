from re import match
from itertools import accumulate

def turn(line):
    (direction, amount) = match('(\\w)(\\d+)', line).groups()
    return int(amount) * {'L': -1, 'R': +1}[direction]


def password():
    entries = open('input/actual.txt').read().splitlines()
    return list(accumulate([50] + list(map(turn, entries)), lambda x, y: (x + y) % 100)).count(0)


print(password())