import copy
import json
import re
import heapq
import sys
import uuid
import sympy as sp
# original a bit slow but works
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
    print(i)
    apx, apy, apz = p1["p"]
    avx, avy, avz = p1["v"]
    for p2 in P[i + 1:]:
        bpx, bpy, bpz = p2["p"]
        bvx, bvy, bvz = p2["v"]

        ta = sp.symbols('ta')
        tb = sp.symbols('tb')

        xa = apx + avx * ta
        ya = apy + avy * ta

        xb = bpx + bvx * tb
        yb = bpy + bvy * tb

        eq1 = sp.Eq(xa, xb)
        eq2 = sp.Eq(ya, yb)

        intersection_time = sp.solve((eq1, eq2), (ta, tb))
        if len(intersection_time) == 2:
            if intersection_time[tb] > 0 and intersection_time[ta] > 0:
                aixp = apx + avx * intersection_time[ta]
                aiyp = apy + avy * intersection_time[ta]
                bixp = bpx + bvx * intersection_time[tb]
                biyp = bpy + bvy * intersection_time[tb]
                if minW <= aixp <= maxW and minW <= aiyp <= maxW and minW <= bixp <= maxW and minW <= biyp <= maxW:
                    output += 1

print(output)
