def to_range(r):
    (start, end) = r.split('-')
    return range(int(start), int(end) + 1)

def is_spoiled(ingredient, fresh_ranges):
    return any(map(lambda r: ingredient in r, fresh_ranges))

def number_of_spoiled_ingredients():
    lines = open('input/actual.txt').read().splitlines()
    blank_idx = lines.index('')
    fresh_ranges = [to_range(l) for l in lines[:blank_idx]]
    ingredients = [int(l) for l in lines[blank_idx + 1:]]
    return [is_spoiled(ingredient, fresh_ranges) for ingredient in ingredients].count(True)

print(number_of_spoiled_ingredients())