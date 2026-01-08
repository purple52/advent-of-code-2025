from functools import reduce, cache

def paths():
    devices = {l.split(':')[0]: tuple(l.strip().split(' ')[1:]) for l in open('input/actual.txt').readlines()}

    @cache
    def find_paths(start, end):
        if start == end:
            return [[end]]
        elif not devices.get(start):
            return []
        else:
            return reduce(list.__add__, [[[start] + p for p in find_paths(d, end)] for d in devices[start]])

    return len(find_paths('svr', 'fft')) * len(find_paths('fft', 'dac')) * len(find_paths('dac', 'out'))

print(paths())