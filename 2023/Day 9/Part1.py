import collections
import functools
import math
import re

input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

input = input.split("\n")

with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)

output = 0
for row in input:
    part = list(map(lambda x: int(x), row.split(" ")))
    diffs = [part]
    for level_index in range(0, len(part)):
        level = []
        for i in range(1, len(diffs[level_index]) ):
            level.append(diffs[level_index][i] - diffs[level_index][i - 1])
        diffs.append(level)
        if not any(x != 0 for x in level):
            break
    add = 0
    for level_index in range(len(diffs)-2,-1,-1):
        add = diffs[level_index][-1] + add
    output += add
print(output)