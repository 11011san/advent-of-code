import math
import re
import aoc_lube
import networkx as nx
import sys

import numpy as np

input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

day = 11
year = 2022

input = aoc_lube.fetch(year, day)

def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x * ans) // math.gcd(x, ans)
    return ans

def part1():
    M = {}
    for dis in input.split("\n\n"):
        dis = dis.splitlines()
        M[dis[0][7]] = {
            "update": dis[2][19:],
            "div": int(dis[3][21:]),
            "t": dis[4][29:],
            "f": dis[5][30:],
            "items": [int(x) for x in dis[1][18:].split(", ")],
            "seen": 0
        }

    for round in range(20):
        for m in M:
            while M[m]["items"]:
                i = M[m]["items"].pop(0)
                M[m]["seen"] += 1
                old = i
                new = eval(M[m]["update"]) // 3
                if new % M[m]["div"] == 0:
                    M[M[m]["t"]]["items"].append(new)
                else:
                    M[M[m]["f"]]["items"].append(new)

    seen = sorted([M[x]['seen'] for x in M])

    return seen[-1] * seen[-2]


def part2():
    M = {}
    for dis in input.split("\n\n"):
        dis = dis.splitlines()
        M[dis[0][7]] = {
            "update": dis[2][19:],
            "div": int(dis[3][21:]),
            "t": dis[4][29:],
            "f": dis[5][30:],
            "items": [int(x) for x in dis[1][18:].split(", ")],
            "seen": 0
        }
    multiple = lcm([M[x]["div"] for x in M])
    for round in range(10000):
        for m in M:
            while M[m]["items"]:
                i = M[m]["items"].pop(0) % multiple
                M[m]["seen"] += 1
                old = i
                new = eval(M[m]["update"])
                if new % M[m]["div"] == 0:
                    M[M[m]["t"]]["items"].append(new)
                else:
                    M[M[m]["f"]]["items"].append(new)

    seen = sorted([M[x]['seen'] for x in M])

    return seen[-1] * seen[-2]


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
