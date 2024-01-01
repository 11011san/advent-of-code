import re
import aoc_lube
import networkx as nx

input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".splitlines()

day = 1
year = 2022
input = aoc_lube.fetch(year, day).splitlines()


def compute():
    global input
    elfs = []
    current = 0
    for row in input:
        if row == "":
            elfs.append(current)
            current = 0
            continue
        current += int(row)
    elfs.sort()
    elfs.reverse()
    return elfs


def part1():
    return compute()[0]


def part2():
    elfs = compute()
    return elfs[0] + elfs[1] + elfs[2]


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
