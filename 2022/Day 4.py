import re
import aoc_lube
import networkx as nx

input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

day = 4
year = 2022

input = aoc_lube.fetch(year, day).splitlines()


def part1():
    count = 0
    for row in input:
        e1, e2 = row.split(',')
        e1 = [int(x) for x in e1.split('-')]
        e2 = [int(x) for x in e2.split('-')]
        if (e1[0] <= e2[0] and e1[1] >= e2[1]) or (e2[0] <= e1[0] and e2[1] >= e1[1]):
            count += 1

    return count


def part2():
    count = 0
    for row in input:
        e1, e2 = row.split(',')
        e1 = [int(x) for x in e1.split('-')]
        e2 = [int(x) for x in e2.split('-')]
        if (e2[0] <= e1[1] <= e2[1] or
                e1[0] <= e2[1] <= e1[1] or
                (e1[0] <= e2[0] and e1[1] >= e2[1]) or
                (e2[0] <= e1[0] and e2[1] >= e1[1])):
            count += 1

    return count


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
