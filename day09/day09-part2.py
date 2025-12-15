from functools import partial
from itertools import combinations

def area(r):
    return (abs(r[0][0] - r[1][0]) + 1) * (abs(r[0][1] - r[1][1]) + 1)

def is_intersect(l, r):
    min_x = min(r[0][0], r[1][0])
    max_x = max(r[0][0], r[1][0])
    min_y = min(r[0][1], r[1][1])
    max_y = max(r[0][1], r[1][1])
    return not ((l[0][0] <= min_x and l[1][0] <= min_x) or
                (l[0][0] >= max_x and l[1][0] >= max_x) or
                (l[0][1] <= min_y and l[1][1] <= min_y) or
                (l[0][1] >= max_y and l[1][1] >= max_y))

def is_valid(lines, r):
    for l in lines:
        if is_intersect(l, r):
            return False
    return True

def valid_rectangles(coords, lines):
    return list(filter(partial(is_valid, lines), combinations(coords, 2)))

def find_largest_rectangle_area(coords):
    lines = list(zip(coords, coords[1:] + coords[:1]))
    return sorted((area(r) for r in valid_rectangles(coords, lines)), reverse=True)[0]

def area_of_largest_rectangle():
    coords = [tuple(int(coord) for coord in l.split(',')) for l in open('input/actual.txt').readlines()]
    return find_largest_rectangle_area(coords)

print(area_of_largest_rectangle())