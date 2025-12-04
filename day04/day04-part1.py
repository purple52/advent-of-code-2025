ADJACENT_OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def is_roll_at(rolls, row, column):
    return False if row < 0 or row >= len(rolls) or column < 0 or column >= len(rolls[row]) else rolls[row][column]

def is_moveable(rolls, row, column):
    adjacent_rolls = [is_roll_at(rolls, row + offset[0], column + offset[1]) for offset in ADJACENT_OFFSETS].count(True)
    return adjacent_rolls < 4

def moveable_rolls_in_row(rolls, row):
    return [is_roll_at(rolls, row, column) and is_moveable(rolls, row, column) for column in range(0, len(rolls[row]))].count(True)

def moveable_rolls():
    rolls = [[cell == '@' for cell in row] for row in open('input/example.txt').read().splitlines()]
    return sum([moveable_rolls_in_row(rolls, row) for row in range(0, len(rolls))])

print(moveable_rolls())