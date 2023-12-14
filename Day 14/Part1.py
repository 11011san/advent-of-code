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
max = len(input)
for y, row in enumerate(input):
    for x, char in enumerate(row):
        if char == "O":
            if y == 0:
                output += max
            else:
                input[y][x] = "."
                for y_drop in range(y - 1, -1, -1):
                    if input[y_drop][x] != ".":
                        input[y_drop + 1][x] = 'O'
                        output += max - (y_drop + 1)
                        break
                    if y_drop == 0:
                        input[y_drop][x] = 'O'
                        output += max - (y_drop)
                        break
for row in input:
    print("".join(row))
print(output)
