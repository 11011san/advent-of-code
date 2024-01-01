import re
import aoc_lube
import networkx as nx

input = [*"""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""]

day = 6
year = 2022

input = [*aoc_lube.fetch(year, day)]


def find_sequence(r):
    global input
    for i in range(r, len(input)):
        start = set(input[i - r:i])
        if len(start) == r:
            return i


def part1():
    return find_sequence(4)


def part2():
    return find_sequence(14)


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
