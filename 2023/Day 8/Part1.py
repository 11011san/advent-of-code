import collections
import functools
import math
import re

input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

input = input.split("\n")

with open("input1.txt", "r") as file_in:
    input = []
    for line in file_in:
        input.append(line)

steps = input[0].replace("\n","")
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
location = "AAA"
while True:
    for step in steps:
        location = nodes[location][step]
        output += 1
        if location == "ZZZ":
            break
    if location == "ZZZ":
        break
print(output)