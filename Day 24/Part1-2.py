import copy
import json
import re
import heapq
import sys
import uuid
from z3 import *

# try to see if using z3 was faster it isn't

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

        ta = Real('ta')
        tb = Real('tb')

        s = Solver()
        s.add(apx + avx * ta == bpx + bvx * tb)
        s.add(apy + avy * ta == bpy + bvy * tb)
        t = s.check()
        m = s.model()
        if t.r == -1:
            continue
        tav, tbv = (0, 0)
        if is_rational_value(m[ta]) and is_rational_value(m[tb]):
            tav = m[ta].as_fraction().numerator / m[ta].as_fraction().denominator
            tbv = m[tb].as_fraction().numerator / m[tb].as_fraction().denominator
        elif is_int_value(m[ta]) and is_rational_value(m[tb]):
            tav = int(m[ta].as_string())
            tbv = int(m[tb].as_string())

        if tav > 0 and tbv > 0:
            aixp = apx + avx * tav
            aiyp = apy + avy * tav
            bixp = bpx + bvx * tbv
            biyp = bpy + bvy * tbv
            if minW <= aixp <= maxW and minW <= aiyp <= maxW and minW <= bixp <= maxW and minW <= biyp <= maxW:
                output += 1

print(output)
