import copy
import json
import re
import heapq
import sys

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
steps = 6

input = open("input1.txt", "r").read().strip()
steps = 64

input = input.split("\n")

output = set()
seen = set()
L = []
for y, row in enumerate(input):
    for x, char in enumerate(row):
        if char == "S":
            L.append((x, y, 0))


def add_step(x, y, s):
    global seen
    global L
    if (x, y) in seen:
        return
    if input[y][x] != "#":
        seen.add((x, y))
        L.append((x, y, s))


while L:
    x, y, s = L.pop(0)
    if s == steps:
        output.add((x, y))
        continue
    if s % 2 == 0:
        output.add((x, y))
    s += 1
    add_step(x + 1, y, s)
    add_step(x - 1, y, s)
    add_step(x, y - 1, s)
    add_step(x, y + 1, s)

print(len(output))
