import re
import aoc_lube
import networkx as nx

input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

day = 3
year = 2022

input = aoc_lube.fetch(year, day).splitlines()


def getPriority(i):
    if i == i.lower():
        return ord(i) - ord('a') + 1
    else:
        return ord(i) - ord('A') + 27


def part1():
    priority = 0
    for row in input:
        p1 = [*row][:(len(row)) // 2]
        p2 = [*row][(len(row)) // 2:]
        for i in p1:
            if i in p2:
                priority += getPriority(i)
                break

    return priority


def part2():
    priority = 0
    group = []
    for row in input:
        group.append([*row])
        if len(group) == 3:
            for i in group[0]:
                if i in group[1] and i in group[2]:
                    priority += getPriority(i)
                    break
            group = []

    return priority


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
