import aoc_lube
import numpy as np

input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()

day = 12
year = 2022

input = aoc_lube.fetch(year, day).splitlines()


def find_start():
    for y, row in enumerate(input):
        if "S" in row:
            return (0, row.index("S"), y)


def find_end():
    for y, row in enumerate(input):
        if "E" in row:
            return (row.index("E"), y)


D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

end_point = find_end()


def find(start):
    P = [start]
    mem = {}
    lenX = len(input[0])
    lenY = len(input)
    while P:
        steps, x, y = P.pop(0)
        pos = (x, y)
        if pos in mem and mem[pos] <= steps:
            continue
        mem[pos] = steps
        if input[y][x] == "E":
            break
        height = ord(input[y][x]) if input[y][x] != "S" else ord('a')
        for d in D:
            npos = tuple(np.add(pos, d))

            if 0 <= npos[0] < lenX and 0 <= npos[1] < lenY:
                if npos in mem:
                    continue
                nhight = ord(input[npos[1]][npos[0]]) if input[npos[1]][npos[0]] != "E" else ord('z')
                if height + 1 >= nhight:
                    P.append((steps + 1, npos[0], npos[1]))
    return mem[end_point] if end_point in mem else 1000000000000


def part1():
    return find(find_start())


def part2():
    best = 1000000
    for y, row in enumerate(input):
        for x, ch in enumerate(row):
            if ch in ['a', 'S']:
                path = find((0, x, y))
                if path < best:
                    best = path
    return best


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
