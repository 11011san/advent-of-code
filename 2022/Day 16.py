import heapq
import re
import time

import aoc_lube
import networkx as nx

input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

day = 16
year = 2022
input = aoc_lube.fetch(year, day)
input = input.splitlines()


def getData():
    V = {}
    G = nx.DiGraph()
    for row in input:
        v = row[6:8]
        V[v] = int(row.split(";")[0][23:])
        for v1 in row.split(";")[1][23:].strip().split(", "):
            G.add_edge(v, v1, capacity=1.0)
    return V, {x[0]: x[1] for x in nx.all_pairs_shortest_path_length(G)}


def _step1(time, pos, w, D, V):
    for v in w:
        if D[pos][v] < time:
            yield (time - D[pos][v] - 1) * V[v] + step1(time - D[pos][v] - 1, v, w - {v}, D, V)
    return 0


def step1(time, pos, w, D, V):
    if time <= 0:
        return 0
    return max(_step1(time, pos, w, D, V), default=0)


def part1():
    V, D = getData()
    W = set([x if V[x] > 0 else "" for x in V])
    W.remove("")
    return step1(30, "AA", W, D, V)


def _step2(time, posM, sM, posE, sE, w, D, V):
    if sM == 0:
        for vm in w:
            if D[posM][vm] < time:
                if sE == 0:
                    for ve in w - {vm}:
                        if D[posE][ve] < time:
                            newTime = max((time - 1 - D[posM][vm]), (time - 1 - D[posE][ve]))
                            yield ((time - 1 - D[posM][vm]) * V[vm]) + ((time - 1 - D[posE][ve]) * V[ve]) + step2(
                                newTime, vm, abs((D[posM][vm] + 1) - (time - newTime)), ve,
                                abs((D[posE][ve] + 1) - (time - newTime)), w - {ve, vm}, D, V)
                else:
                    newTime = max((time - 1 - D[posM][vm]), (time - sE))
                    yield ((time - 1 - D[posM][vm]) * V[vm]) + step2(
                        newTime, vm, abs((D[posM][vm] + 1) - (time - newTime)), posE,
                        abs(sE - (time - newTime)), w - {vm}, D, V)
    elif sE == 0:
        for ve in w:
            if D[posE][ve] < time:
                newTime = max((time - sM), (time - 1 - D[posE][ve]))
                yield ((time - 1 - D[posE][ve]) * V[ve]) + step2(
                    newTime, posM, abs(sM - (time - newTime)), ve,
                    abs((D[posE][ve] + 1) - (time - newTime)), w - {ve}, D, V)
    else:
        assert False, "something wrong"


def step2(time, posM, sM, posE, sE, w, D, V):
    if time <= 0:
        return 0
    return max(_step2(time, posM, sM, posE, sE, w, D, V), default=0)


def part2():
    V, D = getData()
    W = set([x if V[x] > 0 else "" for x in V])
    W.remove("")
    return step2(26, "AA", 0, "AA", 0, W, D, V)


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
