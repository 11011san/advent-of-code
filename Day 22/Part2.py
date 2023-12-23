import copy
import json
import re
import heapq
import sys
import uuid

input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

input = open("input1.txt", "r").read().strip()

input = input.split("\n")

H = []
n = "A"
N = []


def incrementName(n):
    if n == '':
        return 'A'
    if n[-1:] != "Z":
        return n[:-1] + chr(ord(n[-1:]) + 1)
    else:
        return incrementName(n[:-1]) + "A"


for b in input:
    s = b.split("~")
    ss = [int(t) for t in s[0].split(",")]
    se = [int(t) for t in s[1].split(",")]
    heapq.heappush(H, (min(se[2], ss[2]), n, ss, se))
    N.append(n)
    n = incrementName(n)

S = {}
S1 = {}
P = {}
while H:
    minZ, name, ss, se = heapq.heappop(H)
    p = []
    if ss == se:  # add all int positions of the starting brick
        p = [ss]
    else:
        for d in range(3):
            if ss[d] != se[d]:
                break
        if ss[d] > se[d]:
            r = range(se[d], ss[d] + 1)
        else:
            r = range(ss[d], se[d] + 1)
        for p1 in r:
            t = ss.copy()
            t[d] = p1
            p.append(t)

    Dz = -1
    ground = False
    for dz in range(minZ + 1):
        for bp in p:
            assert type(bp) == type([]), f"not list bp = {bp}, dz = {dz}, p={p}, se = {se}, ss={ss}, name = {name}"
            if bp[2] - dz == 0:
                ground = True
            if (bp[0], bp[1], bp[2] - dz) in P:
                Dz = dz - 1
                break
        if Dz != -1:
            break
        if ground:
            Dz = dz
            break
    assert Dz != -1, "cant find landing spot"
    for bp in p:
        P[(bp[0], bp[1], bp[2] - Dz)] = name
        if (bp[0], bp[1], bp[2] - Dz - 1) in P and P[(bp[0], bp[1], bp[2] - Dz - 1)] != name:
            if name not in S:
                S[name] = set()
            S[name].add(P[(bp[0], bp[1], bp[2] - Dz - 1)])
            if P[(bp[0], bp[1], bp[2] - Dz - 1)] not in S1:
                S1[P[(bp[0], bp[1], bp[2] - Dz - 1)]] = set()
            S1[P[(bp[0], bp[1], bp[2] - Dz - 1)]].add(name)


# S [A] = [B] A is on top of B
# S1[A] = [B] A is under B

def fall(n, fallList):
    global S1
    global S
    if n not in S1:
        return fallList
    for n1 in S1[n]:
        if len(S[n1] - fallList) > 0:
            continue
        fallList.add(n1)
        fall(n1, fallList)
    return fallList


output = 0
for n in N:
    output += len(fall(n, set([n]))) - 1
print(output)
