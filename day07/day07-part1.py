from collections import namedtuple
from functools import reduce

State = namedtuple('State', 'beams splits')

def to_splitters(line):
    return set(i for i, v in enumerate(line) if v == '^')

def process_row(state, splitters):
    split_points = state.beams & splitters
    new_beams = state.beams - split_points | reduce(set.union, map(lambda p: {p -1, p + 1}, split_points))
    return State(new_beams, state.splits + len(split_points))

def splits():
    lines = [l for l in open('input/actual.txt').read().splitlines()]
    return reduce(process_row, map(to_splitters, lines[2::2]), State({lines[0].index('S')}, 0)).splits

print(splits())