import re
from collections import namedtuple

from numpy import rint
from scipy.optimize import milp, LinearConstraint, Bounds

Machine = namedtuple('Machine', 'target_state buttons')

def find_fewest_button_presses_for_machine(machine):
    num_buttons = len(machine.buttons)
    a = [[int(i in b) for b in machine.buttons] for i in range(len(machine.target_state))]
    result = milp([1] * num_buttons,
                  integrality=[1] * num_buttons,
                  bounds=Bounds(lb=[0] * num_buttons),
                  constraints=LinearConstraint(a,
                                               lb=machine.target_state,
                                               ub=machine.target_state))
    return int(sum(rint(result.x)))

def parse_line(line):
    target_state = [int(i) for i in re.findall(r"\{([^[}]*)}", line)[0].split(',')]
    buttons = [[int(i) for i in b.split(',')] for b in re.findall(r"\(([^[)]*)\)", line)]
    return Machine(target_state, buttons)

def fewest_button_presses():
    machines = [parse_line(l) for l in open('input/actual.txt').readlines()]
    return sum([find_fewest_button_presses_for_machine(m) for m in machines])

print(fewest_button_presses())