from itertools import chain


def to_range(r):
    (start, end) = r.split('-')
    return range(int(start), int(end) + 1)

def factors(n):
    return [i for i in range(1, n//2 + 1) if n % i == 0]

def seq_factor(total_length, seq_length):
    return sum([10 ** (seq_length * t) for t in range(0, total_length//seq_length)])

def is_invalid(product_id):
    total_length = len(str(product_id))
    return any([(product_id % seq_factor(total_length, seq_length)) == 0 for seq_length in factors(total_length)])

def invalid_id_total():
    ranges = map(to_range, open('input/actual.txt').readline().split(','))
    return sum([product_id for product_id in chain.from_iterable(ranges) if is_invalid(product_id)])

print(invalid_id_total())