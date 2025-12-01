from functools import reduce
from re import match

def turn(line):
    (direction, amount) = match('(\\w)(\\d+)', line).groups()
    return int(amount), {'L': -1, 'R': +1}[direction]

def apply_turn(state, this_turn):
    new_pos = state[0] + this_turn[0] * this_turn[1]
    clicks = abs(this_turn[1] * state[0] // 100 - this_turn[1] * new_pos // 100)
    return new_pos, state[1] + clicks

def password():
    entries = open('input/actual.txt').read().splitlines()
    return reduce(apply_turn, map(turn, entries), (50, 0))[1]

print(password())