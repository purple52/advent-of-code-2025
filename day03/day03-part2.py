def find_best_batteries(bank, num_batteries_to_find):
    if num_batteries_to_find == 0:
        return []
    search_space = bank[:-num_batteries_to_find + 1] if num_batteries_to_find > 1 else bank
    idx = search_space.index(max(search_space))
    return [bank[idx]] + find_best_batteries(bank[idx + 1:], num_batteries_to_find - 1)

def total_output_joltage():
    banks = [[int(i) for i in b] for b in open('input/actual.txt').read().splitlines()]
    return sum([int(''.join(map(str, find_best_batteries(bank, 12)))) for bank in banks])

print(total_output_joltage())