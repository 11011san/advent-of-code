import re
import aoc_lube
import networkx as nx

input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

day = 14
year = 2022

input = aoc_lube.fetch(year, day).splitlines()


def read_walls():
    S = set()
    for row in input:
        pos = (-1, -1)
        for part in row.split(" -> "):
            next = tuple([int(x) for x in part.split(",")])
            if pos == (-1, -1):
                pos = next
                continue
            while pos != next:
                S.add(pos)
                if pos[0] - next[0] != 0:
                    if pos[0] - next[0] > 0:
                        pos = (pos[0] - 1, pos[1])
                    else:
                        pos = (pos[0] + 1, pos[1])
                else:
                    if pos[1] - next[1] > 0:
                        pos = (pos[0], pos[1] - 1)
                    else:
                        pos = (pos[0], pos[1] + 1)
            S.add(pos)
    return S


def add_sand(S, target):
    pos = (500, 0)
    while True:
        if pos[1] == target:
            break
        if (pos[0], pos[1] + 1) not in S:
            pos = (pos[0], pos[1] + 1)
        elif (pos[0] - 1, pos[1] + 1) not in S:
            pos = (pos[0] - 1, pos[1] + 1)
        elif (pos[0] + 1, pos[1] + 1) not in S:
            pos = (pos[0] + 1, pos[1] + 1)
        else:
            break
    return pos


def part1():
    S = read_walls()
    s = 0
    target = max([x[1] for x in S]) + 1
    while True:
        pos = add_sand(S, target)
        if pos[1] == target:
            break
        s += 1
        S.add(pos)
    return s


def part2():
    S = read_walls()
    s = 0
    target = max([x[1] for x in S]) + 1
    while True:
        pos = add_sand(S, target)
        s += 1
        S.add(pos)
        if pos == (500, 0):
            break
    return s


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
