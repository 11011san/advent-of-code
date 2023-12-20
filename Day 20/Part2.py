import copy
import json
import math
import re
import heapq
import sys

# This is a smarter way that I got with some help from hatching https://www.youtube.com/@jonathanpaulson5053
# using the fact they are cyclic

input = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

input = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

input = open("input1.txt", "r").read().strip()

input = input.split("\n")

def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x * ans) // math.gcd(x, ans)
    return ans


output = 0
print("read input")
M = {}
for row in input:
    t = row.split(" -> ")
    if t[0] == "broadcaster":
        M[t[0]] = {"type": "b", "output": t[1].split(", ")}
    else:
        name = t[0][1:]
        type = t[0][0]
        if type == "%":
            M[name] = {"type": type, "output": t[1].split(", "), "state": False}
        else:
            M[name] = {"type": type, "output": t[1].split(", ")}
print("find input to Conjunction")
for m in M:
    if M[m]["type"] == "&":
        M[m]["input"] = {}
        for m1 in M:
            if m in M[m1]["output"]:
                M[m]["input"][m1] = False

for m in M:
    if "rx" in M[m]["output"]:
        output_node = m
        break

init = {}
period = {}
mem = {}
for time in range(1, 10 ** 8):
    high = 0
    low = 1
    L = [("broadcaster", False, "button")]
    if time % 10000 == 0:
        print(f"----- press {time} , found {len(period)}-----")
    while L:
        step = L.pop(0)
        pulse_in = step[1]

        if step[0] in M[output_node]["input"] and not pulse_in:
            if step[0] not in init:
                init[step[0]] = time
            elif step[0] not in period:
                period[step[0]] = time - init[step[0]]

        if step[0] not in M:
            continue
        m = M[step[0]]
        if m["type"] == "b":
            pulse_out = pulse_in
        elif m["type"] == "%":
            if pulse_in:
                continue
            if m["state"]:
                pulse_out = False
            else:
                pulse_out = True
            m["state"] = not m["state"]
        elif m["type"] == "&":
            m["input"][step[2]] = pulse_in
            if all(m["input"].values()):
                pulse_out = False
            else:
                pulse_out = True
        if pulse_out:
            high += len(m["output"])
        else:
            low += len(m["output"])
        for m1 in m["output"]:
            L.append((m1, pulse_out, step[0]))

    if len(period.keys()) == len(M[output_node]["input"].keys()):
        break

print(lcm(period.values()))
