from itertools import chain


def to_range(r):
    (start, end) = r.split('-')
    return range(int(start), int(end) + 1)

def is_valid(product_id):
    digits = len(str(product_id))
    is_valid = digits % 2 == 0 and (product_id % ((10 ** (digits//2)) + 1)) == 0
    return product_id if is_valid else 0

def invalid_ids():
    ranges = map(to_range, open('input/actual.txt').readline().split(','))
    return sum(chain.from_iterable(map(lambda r: map(is_valid, r), ranges)))


print(invalid_ids())