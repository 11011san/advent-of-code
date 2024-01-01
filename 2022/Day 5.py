import re
import aoc_lube
import networkx as nx

input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

day = 5
year = 2022
input = aoc_lube.fetch(year, day)

init, moves = input.split("\n\n")
init = init.splitlines()
moves = moves.splitlines()


def init_stack():
    global init
    stack_number = (len(init[0]) + 1) // 4
    S = [[] for x in range(stack_number)]
    for row in init[:-1]:
        for i in range(stack_number):
            ir = 1 + 4 * i
            if row[ir] == " ":
                continue
            S[i].insert(0, row[ir])
    return S


def read(S):
    result = ""
    for s in S:
        result += s.pop()
    return result


def part1():
    global moves
    S = init_stack()
    for row in moves:
        find = re.match(r"move (\d+) from (\d+) to (\d+)", row)
        s = int(find.group(2)) - 1
        t = int(find.group(3)) - 1
        for i in range(int(find.group(1))):
            S[t].append(S[s].pop())
    return read(S)


def part2():
    global moves
    S = init_stack()
    for row in moves:
        find = re.match(r"move (\d+) from (\d+) to (\d+)", row)
        s = int(find.group(2)) - 1
        t = int(find.group(3)) - 1
        temp = []
        for i in range(int(find.group(1))):
            temp.append(S[s].pop())
        for i in range(int(find.group(1))):
            S[t].append(temp.pop())
    return read(S)


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
