import re
import aoc_lube
import networkx as nx

input = """A Y
B X
C Z""".splitlines()

day = 2
year = 2022
input = aoc_lube.fetch(year, day).splitlines()


table1 = {
    ("A", "X"): 1 + 3,
    ("B", "X"): 1 + 0,
    ("C", "X"): 1 + 6,
    ("A", "Y"): 2 + 6,
    ("B", "Y"): 2 + 3,
    ("C", "Y"): 2 + 0,
    ("A", "Z"): 3 + 0,
    ("B", "Z"): 3 + 6,
    ("C", "Z"): 3 + 3
}

table2 = {
    ("A", "X"): 3 + 0,
    ("B", "X"): 1 + 0,
    ("C", "X"): 2 + 0,
    ("A", "Y"): 1 + 3,
    ("B", "Y"): 2 + 3,
    ("C", "Y"): 3 + 3,
    ("A", "Z"): 2 + 6,
    ("B", "Z"): 3 + 6,
    ("C", "Z"): 1 + 6
}


def part1():
    score = 0
    global input
    global table1
    for row in input:
        e, m = row.split(" ")
        score += table1[(e, m)]

    return score


def part2():
    score = 0
    global input
    global table1
    for row in input:
        e, m = row.split(" ")
        score += table2[(e, m)]

    return score


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
