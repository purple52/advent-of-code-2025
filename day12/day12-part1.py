from collections import namedtuple
from math import prod
from re import findall

Region = namedtuple('Region', 'size target_state')

def to_region(line):
    return Region([int(d) for d in findall(r"(\d+)x(\d+)", line)[0]], [int(i) for i in line.split(' ')[1:]])

def to_shape(lines):
    return [list(map(lambda c: c == '#', l[:-1])) for l in lines]

def estimate_if_valid(region, shapes):
    return sum(region.target_state) * 9 <= prod(region.size)

def valid_regions():
    lines = open('input/actual.txt').readlines()
    regions = [to_region(l) for l in lines[30:]]
    shapes = [to_shape(lines[x+1:x+4]) for x in range(0, 30, 5)]
    return sum([estimate_if_valid(r, shapes) for r in regions])

print(valid_regions())