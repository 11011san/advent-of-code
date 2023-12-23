import copy
import json
import re
import heapq
import sys
import uuid

input = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


input = open("input1.txt", "r").read().strip()

def array_to_string(array):
    result = ""
    for row in array:
        result += "".join(row) + "\n"
    return result[:-1]


def string_to_array(string):
    return [[*x] for x in string.split("\n")]


input = string_to_array(input)
P = []
mem = {}
for x, char in enumerate(input[0]):
    if char == ".":
        P.append((0, x, 0, x, 0))
        break
lenY = len(input)
lenX = len(input[0])
while P:
    assert len(P) < 10, f"to long P {len(P)}, {P}"
    d, x, y, px, py = P.pop()
    if (x, y) in mem and mem[(x, y)] > d:
        continue
    mem[(x, y)] = d
    if input[y][x] == "<":
        if x - 1 == px and y == py:
            continue
        P.append((d + 1, x - 1, y, x, y))
    elif input[y][x] == ">":
        if x + 1 == px and y == py:
            continue
        P.append((d + 1, x + 1, y, x, y))
    elif input[y][x] == "v":
        if x == px and y + 1 == py:
            continue
        P.append((d + 1, x, y + 1, x, y))
    elif input[y][x] == "^":
        if x == px and y - 1 == py:
            continue
        P.append((d + 1, x, y - 1, x, y))
    else:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if x + dx == px and y + dy == py:
                continue
            if not (0 < x + dx < lenX and 0 <= y + dy < lenY):
                continue
            if input[y + dy][x + dx] == "#":
                continue
            P.append((d + 1, x + dx, y + dy, x, y))

y = len(input) - 1
for x, char in enumerate(input[y]):
    if char == ".":
        break
print(mem[(x, y)])
