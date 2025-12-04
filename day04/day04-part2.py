from functools import partial

ADJACENT_OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def is_roll_at(rolls, row, column):
    return False if row < 0 or row >= len(rolls) or column < 0 or column >= len(rolls[row]) else rolls[row][column]

def is_roll_moveable(rolls, row, column):
    return [is_roll_at(rolls, row + offset[0], column + offset[1]) for offset in ADJACENT_OFFSETS].count(True) < 4

def try_to_remove_roll(rolls, row, column):
    if is_roll_at(rolls, row, column) and is_roll_moveable(rolls, row, column):
        rolls[row][column] = False
        return True

def remove_rolls_in_row(rolls, row):
    return [try_to_remove_roll(rolls, row, column) for column in range(0, len(rolls[row]))].count(True)

def sweep(rolls):
    return sum([remove_rolls_in_row(rolls, row) for row in range(0, len(rolls))])

def remove_all_moveable_rolls():
    rolls = [[cell == '@' for cell in row] for row in open('input/actual.txt').read().splitlines()]
    return sum(iter(partial(sweep, rolls), 0))

print(remove_all_moveable_rolls())