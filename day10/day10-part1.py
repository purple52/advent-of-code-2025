import re
from collections import namedtuple
from functools import reduce
from itertools import count, combinations_with_replacement

Machine = namedtuple('Machine', 'target_state buttons')

def generates_target_state(machine, presses):
    return machine.target_state == reduce(lambda s, p: list(map(lambda i: i[0] ^ i[1], zip(s, p))), presses, [False] * len(machine.target_state))

def find_fewest_button_presses_for_machine(machine):
    for i in count(start=1):
        for presses in combinations_with_replacement(machine.buttons, i):
            if generates_target_state(machine, presses):
                return i
    return None

def parse_line(line):
    target_state = [{'#': True, '.': False}[i] for i in re.findall(r"\[([^[\]]*)]", line)[0]]
    to_binary_list = lambda b: reduce(lambda l, x: [True if i == int(x) else v for i, v in enumerate(l)], b.split(','), [False] * len(target_state))
    buttons = [to_binary_list(b) for b in re.findall(r"\(([^[)]*)\)", line)]
    return Machine(target_state, buttons)

def fewest_button_presses():
    machines = [parse_line(l) for l in open('input/actual.txt').readlines()]
    return sum([find_fewest_button_presses_for_machine(m) for m in machines])

print(fewest_button_presses())