
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


def check_pos(input, pos):
    for index in pos:
        badness = 0
        for row in input:
            split = split_pattern(row, index)
            for i, char in enumerate(split[0][::-1]):
                if char != split[1][i]:
                    badness += 1
                    if badness > 1:
                        break

            if badness > 1:
                break
        if badness == 1:
            print(index)
            return index
    return 0


output = 0

for pattern in range(0, len(input), 1):
    ver_input = input[pattern].split("\n")
    hor_input = [''.join(s) for s in zip(*input[pattern].split("\n"))]
    ver_possible = range(1, len(ver_input[0]))
    hor_possible = range(1, len(hor_input[0]))
    ver_output = check_pos(ver_input, ver_possible)
    hor_output = check_pos(hor_input, hor_possible) * 100
    output += ver_output + hor_output

print(output)
