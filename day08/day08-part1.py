from collections import namedtuple
from functools import reduce
from itertools import chain, repeat
from math import prod

from scipy.spatial import KDTree

JunctionBoxPair = namedtuple('JunctionBoxPair', 'box nearest_box distance' )

def find_nearest_pairs(junction_boxes):
    to_junction_box_pair = lambda x: JunctionBoxPair(int(x[0]), int(x[1]), x[2])
    distances, nearest_boxes  = KDTree(junction_boxes).query(junction_boxes, k=len(junction_boxes))
    pairs = chain(*map(lambda x: zip(repeat(x[0]), x[1][0][1:], x[1][1][1:]), enumerate(zip(nearest_boxes, distances))))
    return sorted(map(to_junction_box_pair,  pairs), key=lambda pair: pair.distance)[::2]

def merge_into_circuits(circuits, pair):
    circuit_x = next((i for i, circuit in enumerate(circuits) if pair.box in circuit))
    circuit_y = next((i for i, circuit in enumerate(circuits) if pair.nearest_box in circuit))

    if circuit_x != circuit_y:
        circuits[circuit_x].update(circuits[circuit_y])
        del circuits[circuit_y]

    return circuits

def find_circuits_between_closest_boxes(junction_boxes, num_connections):
    nearest_pairs = find_nearest_pairs(junction_boxes)
    circuits = reduce(merge_into_circuits, nearest_pairs[:num_connections], [{i} for i in range(0, len(nearest_pairs))])
    return circuits

def multiply_largest_circuits(num_connections, num_circuits):
    junction_boxes = list(map(lambda l: list(map(int, l.split(','))), open('input/actual.txt').read().splitlines()))
    circuits = find_circuits_between_closest_boxes(junction_boxes, num_connections)
    return prod(map(len, sorted(circuits, key=len, reverse=True)[:num_circuits]))

print(multiply_largest_circuits(1000, 3))