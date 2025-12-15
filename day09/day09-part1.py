from itertools import combinations


def area(r):
    return (abs(r[0][0] - r[1][0]) + 1) * (abs(r[0][1] - r[1][1]) + 1)

def find_largest_rectangle_area(coords):
    return sorted((area(c) for c in combinations(coords, 2)), reverse=True)[0]

def area_of_largest_rectangle():
    coords = [tuple(int(coord) for coord in l.split(',')) for l in open('input/actual.txt').readlines()]
    return find_largest_rectangle_area(coords)

print(area_of_largest_rectangle())