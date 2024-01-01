import copy
import re
import heapq
import sys

input = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

input = open("input1.txt", "r").read().strip()

input = input.split("\n\n")

F = {}

for flow in input[0].split("\n"):
    s = flow.split("{")
    name = s[0]
    rules = []
    for rule in s[1][:-1].split(","):
        if ":" in rule:
            t = rule.split(":")
            rules.append((t[0][:1], t[0][1:2], int(t[0][2:]), t[1]))
        else:
            rules.append(("x", ">", 0, rule))
    F[name] = rules

output = 0
for row in input[1].split("\n"):
    t = row[1:-1].split(",")
    part = {}
    for a in t:
        aa = a.split("=")
        part[aa[0]] = int(aa[1])

    pos = "in"
    while True:
        if pos == "A":
            for a in part.values():
                output += a
            break
        elif pos == "R":
            break
        for rule in F[pos]:
            if rule[1] == ">":
                if part[rule[0]] > rule[2]:
                    pos = rule[3]
                    break
            elif rule[1] == "<":
                if part[rule[0]] < rule[2]:
                    pos = rule[3]
                    break
            else:
                assert False, f"didn't understand rule {rule}"

print(output)
