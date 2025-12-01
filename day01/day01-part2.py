from collections import namedtuple
from functools import reduce
from re import match

Turn = namedtuple('Turn', 'amount direction')
State = namedtuple('State', 'position clicks')

def turn(line):
    (direction, amount) = match('(\\w)(\\d+)', line).groups()
    return Turn(int(amount), {'L': -1, 'R': +1}[direction])

def apply_turn(state, this_turn):
    new_position = state.position + this_turn.amount * this_turn.direction
    clicks = abs(this_turn.direction * state.position // 100 - this_turn.direction * new_position // 100)
    return State(new_position, state.clicks + clicks)

def password():
    entries = open('input/actual.txt').read().splitlines()
    return reduce(apply_turn, map(turn, entries), State(50, 0)).clicks

print(password())