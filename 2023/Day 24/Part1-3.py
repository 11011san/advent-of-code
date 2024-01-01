import copy
import json
import re
import heapq
import sys
import uuid
from z3 import *

# using the correct equations match faster got from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/24.py

input = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

minW = 7
maxW = 27

input = open("input1.txt", "r").read().strip()
minW = 200000000000000
maxW = 400000000000000

input = input.split("\n")

P = []
for row in input:
    s1 = row.split(" @ ")
    p = [int(x) for x in s1[0].split(", ")]
    v = [int(x) for x in s1[1].split(", ")]
    P.append({"p": p, "v": v})

output = 0

for i, p1 in enumerate(P):
    ap1x, ap1y, ap1z = p1["p"]
    avx, avy, avz = p1["v"]
    ap2x = ap1x + avx
    ap2y = ap1y + avy
    for p2 in P[i + 1:]:
        bp1x, bp1y, bp1z = p2["p"]
        bvx, bvy, bvz = p2["v"]
        bp2x = bp1x + bvx
        bp2y = bp1y + bvy

        den = ((ap1x - ap2x) * (bp1y - bp2y) - (ap1y - ap2y) * (bp1x - bp2x))
        if den != 0:

            ix = ((ap1x * ap2y - ap1y * ap2x) * (bp1x - bp2x) - (ap1x - ap2x) * (bp1x * bp2y - bp1y * bp2x)) / (
                    (ap1x - ap2x) * (bp1y - bp2y) - (ap1y - ap2y) * (bp1x - bp2x))
            iy = ((ap1x * ap2y - ap1y * ap2x) * (bp1y - bp2y) - (ap1y - ap2y) * (bp1x * bp2y - bp1y * bp2x)) / (
                    (ap1x - ap2x) * (bp1y - bp2y) - (ap1y - ap2y) * (bp1x - bp2x))
            validA = (ix > ap1x) == (ap2x > ap1x)
            validB = (ix > bp1x) == (bp2x > bp1x)

            if minW <= ix <= maxW and minW <= iy <= maxW and validA and validB:
                output += 1

print(output)
