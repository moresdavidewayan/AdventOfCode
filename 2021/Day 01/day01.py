import pathlib

def count(values: list[int], n: int) -> int:
    counter: int = 0
    for i in range(n, len(values)):
        if values[i] > values[i - n]:
            counter += 1
    return counter

values: list[int] = [int(line) for line in open(pathlib.Path(__file__).parent / 'input.txt', 'r')]

print(f'Part 1: {count(values, 1)}.')
print(f'Part 2: {count(values, 3)}.')