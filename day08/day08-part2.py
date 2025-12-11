from collections import namedtuple
from itertools import chain, repeat

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

def connect_circuits(junction_boxes):
    nearest_pairs = find_nearest_pairs(junction_boxes)
    circuits = [{i} for i in range(0, len(junction_boxes))]
    for pair in nearest_pairs:
        circuits = merge_into_circuits(circuits, pair)
        if len(circuits) == 1:
            return pair

    return None

def multiply_final_x_coordinates():
    junction_boxes = list(map(lambda l: list(map(int, l.split(','))), open('input/actual.txt').read().splitlines()))
    final_pair = connect_circuits(junction_boxes)
    return junction_boxes[final_pair.box][0] * junction_boxes[final_pair.nearest_box][0]

print(multiply_final_x_coordinates())