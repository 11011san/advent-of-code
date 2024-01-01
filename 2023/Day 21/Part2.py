import copy
import json
import re
import heapq
import sys
import math

# This is a smarter way that I got with some help from hatching https://www.youtube.com/@jonathanpaulson5053
# using the fact they are cyclic

input = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
steps = 5000

input = open("input1.txt", "r").read().strip()
steps = 26501365

raw = input
input = input.split("\n")
lenX = len(input[0])
lenY = len(input)

grid_size = 3
D = {}
L = []
for y, row in enumerate(input):
    for x, char in enumerate(row):
        if char == "S":
            L.append((x, y, 0))


def add_step(x, y, s):
    global seen
    global L
    if input[y % lenY][x % lenX] != "#":
        L.append((x, y, s))


print("making map")
while L:
    x, y, s = L.pop(0)
    if (x, y) in D:
        continue
    if abs(x // lenX) > grid_size or abs(y // lenY) > grid_size:
        continue
    D[(x, y)] = s
    if s == steps:
        continue
    s += 1
    add_step(x + 1, y, s)
    add_step(x - 1, y, s)
    add_step(x, y - 1, s)
    add_step(x, y + 1, s)

output = 0

mem = {}


def solve(s, edge):
    global steps
    global lenX
    multiplyer = (steps - s) // lenX
    if (s, edge) in mem:
        return mem[(s, edge)]
    result = 0
    for x in range(1, multiplyer + 1):
        if s + lenX * x <= steps and (s + lenX * x) % 2 == (steps % 2):
            result += ((x + 1) if not edge else 1)
    mem[(s, edge)] = result
    return result


print("computing")

for point in D:
    s = D[point]
    x, y = point
    if s % 2 == steps % 2 and s <= steps:
        output += 1
    if abs(x // lenX) == grid_size and abs(y // lenY) == grid_size:
        output += solve(s, False)
    elif abs(x // lenX) == grid_size or abs(y // lenY) == grid_size:
        output += solve(s, True)

print(output)