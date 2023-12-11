import collections
import functools
import math
import re

# This is a smarter way that I got with some help from hatching https://www.youtube.com/@jonathanpaulson5053
# using the fact they are cyclic
input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

input = open("input1.txt", "r").read().strip()

input = input.split("\n")


steps = input[0].replace("\n", "")
nodes = {}
for line in input[2:]:
    found = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)$", line)
    if len(found.groups()) == 3:
        nodes[str(found.group(1))] = {
            "L": str(found.group(2)),
            "R": str(found.group(3))
        }
print(nodes)

output = 0
locations = []
for node in nodes.keys():
    if node.endswith("A"):
        locations.append(node)
print(f"found start locations {len(locations)} they are {locations}")


def found_end():
    global locations
    global output
    for i, location in enumerate(locations):
        if location.endswith("Z"):
            T[i] = output

    return len(T) == len(locations)


def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x * ans) // math.gcd(x, ans)
    return ans


T = {}
found = False
while True:
    for step in steps:
        for index, location in enumerate(locations):
            locations[index] = nodes[location][step]
        output += 1
        if found_end():
            found = True
            break
        if output % 1000 == 0:
            print(output)
    if found:
        break
print(lcm(T.values()))
