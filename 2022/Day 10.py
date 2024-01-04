import re
import aoc_lube
import networkx as nx

input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

day = 10
year = 2022


input = aoc_lube.fetch(year, day).splitlines()


def part1():
    sum = 0
    X = 1
    c = 1
    check = 20
    check_step = 40
    for row in input:
        if row == "noop":
            c += 1
            if c == check:
                sum += check * X
                check += check_step
        else:
            c += 1
            if c == check:
                sum += check * X
                check += check_step
            X += int(row.split(" ")[1])
            c += 1
            if c == check:
                sum += check * X
                check += check_step
    return sum


def part2():
    X = 1
    c = -1
    width = 40
    high = 6
    S = [["." for _ in range(width)] for _ in range(high)]
    for row in input:
        if row == "noop":
            c += 1
            if c % width - 1 <= X <= c % width + 1:
                S[(c // width) % high][c % width] = "#"
            else:
                S[(c // width) % high][c % width] = "."
        else:
            c += 1
            if c % width - 1 <= X <= c % width + 1:
                S[(c // width) % high][c % width] = "#"
            else:
                S[(c // width) % high][c % width] = "."
            c += 1
            if c % width - 1 <= X <= c % width + 1:
                S[(c // width) % high][c % width] = "#"
            else:
                S[(c // width) % high][c % width] = "."
            X += int(row.split(" ")[1])
    image = ""
    for row in S:
        image += "".join(row)
        image += '\n'
    print(image)
    return


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=lambda: "RGLRBZAU")

###...##..#....###..###..####..##..#..#.
#..#.#..#.#....#..#.#..#....#.#..#.#..#.
#..#.#....#....#..#.###....#..#..#.#..#.
###..#.##.#....###..#..#..#...####.#..#.
#.#..#..#.#....#.#..#..#.#....#..#.#..#.
#..#..###.####.#..#.###..####.#..#..##..