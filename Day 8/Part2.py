import collections
import functools
import math
import re
# This is bruteforce and takes long time
input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

input = input.split("\n")

with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)

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
    for location in locations:
        if not location.endswith("Z"):
            return False
    return True

found = False
while True:
    for step in steps:
        for index,location in enumerate(locations):
            locations[index] = nodes[location][step]
        output += 1
        if found_end():
            found = True
            break
        if output % 1000 == 0:
            print(output)
    if found:
        break
print(output)
