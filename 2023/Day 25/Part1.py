
import re
import aoc_lube
import networkx as nx

input = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr""".splitlines()

# input = open("input1.txt", "r").read().splitlines()
input = aoc_lube.fetch(2023,25).splitlines()



G = nx.DiGraph()
E = {}
for row in input:
    cs = re.findall(r"\w{3}", row)
    n1 = cs[0]
    if n1 not in E:
        E[n1] = set()
    for n2 in cs[1:]:
        if n2 not in E:
            E[n2] = set()
        E[n1].add(n2)
        E[n2].add(n1)


for n1 in E:
    for n2 in E[n1]:
        G.add_edge(n1, n2, capacity=1.0)
        G.add_edge(n2, n1, capacity=1.0)


for n1 in E:
    for n2 in E:
        if n1 == n2:
            continue
        minCut, partition = nx.minimum_cut(G, n1, n2)
        if minCut == 3:
            print(len(partition[0])*len(partition[1]))
            exit(0)

