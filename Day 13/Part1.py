input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

input = open("input1.txt", "r").read().strip()

input = input.split("\n\n")


def split_pattern(input, split):
    left = input[:split]
    right = input[split:]
    if len(left) > len(right):
        left = left[len(left) - len(right):]
    else:
        right = right[:len(left)]
    return left, right


def find_possible(input):
    length = len(input)
    pos = []
    for i in range(1, length):
        split = split_pattern(input, i)
        if split[0] == split[1][::-1]:
            pos.append(i)
    return pos


def check_pos(input, pos):
    for index in pos:
        found = True
        for row in input:
            split = split_pattern(row, index)
            if split[0] != split[1][::-1]:
                found = False
                break
        if found:
            print(index)
            return index
    return 0


output = 0

for pattern in range(0, len(input), 1):
    ver_input = input[pattern].split("\n")
    hor_input = [''.join(s) for s in zip(*input[pattern].split("\n"))]
    ver_possible = find_possible(ver_input[0])
    hor_possible = find_possible(hor_input[0])
    ver_output = check_pos(ver_input, ver_possible)
    hor_output = check_pos(hor_input, hor_possible) * 100
    output += max(ver_output, hor_output)

print(output)
