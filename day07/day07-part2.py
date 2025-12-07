from functools import reduce, partial

def process_splitter(timelines, s):
    apply = lambda t: 0 if t[0] == s else t[1] + timelines[s] if abs(t[0] - s) == 1 else t[1]
    return list(map(apply, enumerate(timelines)))

def process_row(timelines, splitters):
    return reduce(process_splitter, splitters, timelines)

def total_timelines():
    lines = [l for l in open('input/actual.txt').read().splitlines()]
    initial_timelines = list(map(partial(str.count, 'S'), lines[0]))
    to_splitters = lambda l: set(i for i, v in enumerate(l) if v == '^')
    return sum(reduce(process_row, map(to_splitters, lines[2::2]), initial_timelines))

print(total_timelines())