import re
import aoc_lube
import networkx as nx
import numpy as np

input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()

day = 9
year = 2022

input = aoc_lube.fetch(year, day).splitlines()
D = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0)
}


def update(h, t):
    if not (-1 <= h[0] - t[0] <= 1 and -1 <= h[1] - t[1] <= 1):
        if h[0] != t[0] and h[1] != t[1]:
            t = (t[0] + (1 if t[0] < h[0] else -1), t[1] + (1 if t[1] < h[1] else -1))
        elif h[0] == t[0]:
            t = (t[0], t[1] + (1 if t[1] < h[1] else -1))
        else:
            t = (t[0] + (1 if t[0] < h[0] else -1), t[1])
    return t


def compute(rope):
    h = (0, 0)
    t = [(0, 0) for x in range(rope)]
    T = set()
    T.add(t[rope - 1])
    for row in input:
        d, l = row.split(" ")
        for i in range(int(l)):
            h = tuple(np.add(h, D[d]))
            t[0] = update(h, t[0])
            for i in range(1, rope):
                t[i] = update(t[i - 1], t[i])
            T.add(t[rope - 1])
    return len(T)


def part1():
    return compute(1)


def part2():
    return compute(9)


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
