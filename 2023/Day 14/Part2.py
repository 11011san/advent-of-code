input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

input = open("input1.txt", "r").read().strip()

input = input.split("\n")

input = [[*x] for x in input]

output = 0
max_y = len(input)
max_x = len(input[0])


def hash():
    global input
    return "\n".join(["".join(x) for x in input])


def get_score(map):
    map_array = map.split("\n")
    score = 0
    max_y = len(map_array)
    for y, row in enumerate(map_array):
        for char in row:
            if char == "O":
                score += max_y - y
    return score


def get_key(val):
    global mem
    for key, value in mem.items():
        if val == value:
            return key
    return "key doesn't exist"


result = ""
mem = {}
mem[hash()] = 0,
for time in range(1, 1000000000 + 1):
    for y, row in enumerate(input):  # north
        for x, char in enumerate(row):
            if char == "O":
                if y != 0:
                    input[y][x] = "."
                    for y_drop in range(y - 1, -1, -1):
                        if input[y_drop][x] != ".":
                            input[y_drop + 1][x] = 'O'
                            break
                        if y_drop == 0:
                            input[y_drop][x] = 'O'
                            break

    for y, row in enumerate(input):  # west
        for x, char in enumerate(row):
            if char == "O":
                if x != 0:
                    input[y][x] = "."
                    for x_drop in range(x - 1, -1, -1):
                        if input[y][x_drop] != ".":
                            input[y][x_drop + 1] = 'O'
                            break
                        if x_drop == 0:
                            input[y][x_drop] = 'O'
                            break

    for y, row in enumerate(reversed(input)):  # South
        act_y = max_y - y - 1
        for x, char in enumerate(row):
            if char == "O":
                if act_y != max_y - 1:
                    input[act_y][x] = "."
                    for y_drop in range(act_y + 1, max_y):
                        if input[y_drop][x] != ".":
                            input[y_drop - 1][x] = 'O'
                            break
                        if y_drop == max_y - 1:
                            input[y_drop][x] = 'O'
                            break

    for y, row in enumerate(input):  # east
        for x, char in enumerate(reversed(row)):
            act_x = max_x - x - 1
            if char == "O":
                if act_x != max_x - 1:
                    input[y][act_x] = "."
                    for x_drop in range(act_x + 1, max_x):
                        if input[y][x_drop] != ".":
                            input[y][x_drop - 1] = 'O'
                            break
                        if x_drop == max_x - 1:
                            input[y][x_drop] = 'O'
                            break
    current = hash()
    if current in mem:
        offset = (1000000000 - ((1000000000 - time) // (time - mem[current])) * (time - mem[current])) % time
        result = get_key(mem[current] + offset)
        break
    mem[current] = time

for row in input:
    print("".join(row))
print(f"{get_score(result)}")
