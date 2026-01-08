from functools import reduce

def find_paths_from(devices, path, current):
    if current == 'out':
        print(path + [current])
        return [path + [current]]
    elif not devices[current]:
        return []
    else:
        return reduce(list.__add__, [find_paths_from(devices, path + [current], o) for o in devices[current]])

def find_paths(devices):
    return find_paths_from(devices, [], 'you')

def paths():
    devices = {l.split(':')[0]: l.strip().split(' ')[1:] for l in open('input/actual.txt').readlines()}
    return len(find_paths(devices))

print(paths())