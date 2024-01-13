import functools
import re
import aoc_lube
import networkx as nx

input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

day = 13
year = 2022


input = aoc_lube.fetch(year, day)


def compare(l, r):
    if type(l) != type(r):
        if type(l) == int:
            l = [l]
        if type(r) == int:
            r = [r]
    if type(l) == int:
        if l == r:
            return None
        else:
            return l < r
    else:
        for i in range(len(l)):
            if len(r) == i:
                return False
            ans = compare(l[i], r[i])
            if ans is None:
                continue
            return ans
        return True


def compare_sort(l, r):
    if compare(l, r):
        return -1
    else:
        return 1


def part1():
    result = 0
    for i, row in enumerate(input.split("\n\n")):
        l, r = [eval(x) for x in row.split('\n')]
        ans = compare(l, r)
        if ans:
            result += i + 1
    return result


def part2():
    L = [[[2]], [[6]]]
    for i, row in enumerate(input.split("\n")):
        if row == '':
            continue
        L.append(eval(row))
    L.sort(key=functools.cmp_to_key(compare_sort))
    L.sort(key=functools.cmp_to_key(compare_sort))
    return (L.index([[2]])+1) * (L.index([[6]])+1)


print(part22())
aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
