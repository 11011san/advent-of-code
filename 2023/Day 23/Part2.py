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

lenY = len(input)
lenX = len(input[0])

for x, char in enumerate(input[0]):
    if char == ".":
        start = (x, 0)
        break

for x, char in enumerate(input[lenY - 1]):
    if char == ".":
        end = (x, lenY - 1)
        break
P.append((start, -1, start, start))
N = {}
while P:
    # assert len(P) < 10, f"to long P {len(P)}, {P}"
    pos, d, prev, source = P.pop()

    cross = []
    if pos == end:
        if source not in N:
            N[source] = {}
        if pos not in N:
            N[pos] = {}
        N[source][pos] = d
        N[pos][source] = d
        continue

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = pos[0] + dx
        ny = pos[1] + dy
        if not (0 < nx < lenX and 0 <= ny < lenY):
            continue
        if input[ny][nx] == "#":
            continue
        if (nx, ny) == prev:
            continue
        cross.append((nx, ny))
    if len(cross) == 0:
        continue
    elif len(cross) == 1:
        P.append((cross[0], d + 1, pos, source))
    else:
        if source not in N:
            N[source] = {}
        if pos not in N:
            N[pos] = {}
        N[source][pos] = d
        N[pos][source] = d
        if len(N[pos]) == len(cross) + 1:
            continue
        for next in cross:
            P.append((next, 0, pos, pos))

P.append((start, 0, []))
output = 0
mem = {}
while P:
    # assert len(P) < 10, f"to long P {len(P)}, {P}"
    pos, d, path = P.pop()
    if pos == end:
        if output < d:
            output = d
        continue
    for next in N[pos]:
        if next in path:
            continue
        path1 = path.copy()
        path1.append((pos))
        P.append((next, d + N[pos][next] + 1, path1))

print(output)
