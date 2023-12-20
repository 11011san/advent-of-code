import copy
import json
import re
import heapq
import sys

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
mem = {}
for time in range(0, 1000):
    high = 0
    low = 1
    L = [("broadcaster", False, "button")]
    print(f"----- press {time + 1} -----")
    while L:
        step = L.pop(0)
        pulse_in = step[1]
        if step[0] not in M:
            continue
        m = M[step[0]]
        if pulse_in:
            print(f"{step[2]} -high-> {step[0]}")
        else:
            print(f"{step[2]} -low-> {step[0]}")
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

    hash = json.dumps(M, sort_keys=True)
    if hash in mem:
        break
    mem[hash] = (time, high, low)

T = {}
for hash in mem:
    T[mem[hash][0]] = (mem[hash])

high = 0
low = 0
for press in range(0, 1000):
    high += T[press % len(T)][1]
    low += T[press % len(T)][2]

print(high*low)
