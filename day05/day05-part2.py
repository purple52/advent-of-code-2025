from bisect import bisect_left
from functools import reduce


def to_range(r):
    (start, end) = r.split('-')
    return range(int(start), int(end) + 1)

def merge_range(ranges, r):
    pos = bisect_left(ranges, r.start, key=lambda i: i.stop)
    replace = bisect_left(ranges, r.stop, lo=pos, key=lambda i: i.start) - pos
    new_range = range(min(r.start, ranges[pos].start), max(r.stop, ranges[pos + replace - 1].stop)) if replace else r
    return ranges[:pos] + [new_range] + ranges[pos + replace:]

def merge_ranges(fresh_ranges):
    return reduce(merge_range, fresh_ranges, [])

def count_fresh_ingredients(fresh_ranges):
    return sum(map(len, fresh_ranges))

def number_of_fresh_ingredients():
    lines = open('input/actual.txt').read().splitlines()
    return count_fresh_ingredients(merge_ranges([to_range(l) for l in lines[:lines.index('')]]))

print(number_of_fresh_ingredients())