def joltage(bank):
    first_idx = bank.index(max(bank[:-1]))
    second_idx = bank.index(max(bank[first_idx + 1:]))
    return bank[first_idx] * 10 + bank[second_idx]

def total_output_joltage():
    banks = map(lambda b: list(map(int, b)), open('input/actual.txt').read().splitlines())
    return sum(map(joltage, banks))

print(total_output_joltage())