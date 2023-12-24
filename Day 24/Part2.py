import copy
import json
import re
import heapq
import sys
import uuid
from z3 import *
import time

# used synpy on first attempt was way too slow to solve it changed to z3 match faster

input = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
start = time.time()
input = open("input1.txt", "r").read().strip()

input = input.split("\n")

P = []
for row in input:
    s1 = row.split(" @ ")
    p = [int(x) for x in s1[0].split(", ")]
    v = [int(x) for x in s1[1].split(", ")]
    P.append({"p": p, "v": v})

T = []
E = []
px = Int('px')
py = Int('py')
pz = Int('pz')
vx = Int('vx')
vy = Int('vy')
vz = Int('vz')
T.append(px)
T.append(py)
T.append(pz)
T.append(vx)
T.append(vy)
T.append(vz)

for i, p1 in enumerate(P):
    apx, apy, apz = p1["p"]
    avx, avy, avz = p1["v"]
    ti = Int(f't{i}')
    T.append(ti)
    E.append(apx + avx * ti == px + vx * ti)
    E.append(apy + avy * ti == py + vy * ti)
    E.append( apz + avz * ti == pz + vz * ti)

s = Solver()
s.add(E)
s.check()
m = s.model()

print(f"time = {time.time() - start}")

print(f"{m[px].as_string()}, {m[py].as_string()}, {m[pz].as_string()} @ {m[vx].as_string()}, {m[vy].as_string()}, {m[vz].as_string()}")
print(f"answer = {int(m[px].as_string())+int(m[py].as_string())+int(m[pz].as_string())}")
