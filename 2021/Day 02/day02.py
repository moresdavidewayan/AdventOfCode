import pathlib

def get_result(moves: list[str], first_part: bool) -> int:
    aim: int = 0
    depth: int = 0
    horizontal_position: int = 0
    for movement in moves:
        action, length = movement.split()
        length = int(length)
        match action:
            case 'forward':
                horizontal_position += length
                if not first_part:
                    depth += aim * length
            case 'up':
                aim -= length
                depth -= (length if first_part else 0)
            case 'down':
                aim += length
                depth += (length if first_part else 0)
    return depth * horizontal_position

moves: list[str] = open(pathlib.Path(__file__).parent / 'input.txt', 'r').readlines()

print(f'Part 1: {get_result(moves, True)}.')
print(f'Part 2: {get_result(moves, False)}.')