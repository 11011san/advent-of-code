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


def find(part, flow):
    result = 0
    if flow == "R":
        return 0
    if flow == "A":
        result = 1
        for a in part.values():
            result *= a[1] - a[0] + 1
        return result
    global F
    for rule in F[flow]:
        if rule[1] == ">":
            if part[rule[0]][0] > rule[2]:
                result += find(part, rule[3])
            elif part[rule[0]][1] < rule[2]:
                continue
            else:
                part_temp = part.copy()
                part_temp[rule[0]] = (rule[2] + 1, part_temp[rule[0]][1])
                part[rule[0]] = (part[rule[0]][0], rule[2])
                result += find(part_temp, rule[3])
        elif rule[1] == "<":
            if part[rule[0]][1] < rule[2]:
                result += find(part, rule[3])
            elif part[rule[0]][0] > rule[2]:
                continue
            else:
                part_temp = part.copy()
                part_temp[rule[0]] = (part_temp[rule[0]][0], rule[2] - 1)
                part[rule[0]] = (rule[2], part[rule[0]][1])
                result += find(part_temp, rule[3])
        else:
            assert False, f"didn't understand {rule}"
    return result


output = find({"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}, "in")

print(output)
