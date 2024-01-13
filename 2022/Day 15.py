import re
import aoc_lube
import networkx as nx

input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

day = 15
year = 2022
input = aoc_lube.fetch(year, day)

input = input.splitlines()


def part1():
    S = []
    y = 2000000
    # y = 10
    for row in input:
        s, b = re.findall(r"x=([\d-]+), y=([\d-]+)", row)
        s = (int(s[0]), int(s[1]), abs(int(s[0]) - int(b[0])) + abs(int(s[1]) - int(b[1])))
        if abs(s[1] - y) <= s[2]:
            S.append(s)
    X = set()
    for s in S:
        for xd in range(s[2] - abs(s[1] - y) + 1):
            X.add(s[0] + xd)
            X.add(s[0] - xd)

    return len(X) - 1


def no_coverage(x, y, S, target):
    if not (0 <= x <= target and 0 <= y <= target):
        return False
    for sx, sy, d in S:
        if abs(sx - x) + abs(sy - y) <= d:
            return False
    return True


def part2():
    S = []
    target = 4000000
    for row in input:
        s, b = re.findall(r"x=([\d-]+), y=([\d-]+)", row)
        s = (int(s[0]), int(s[1]), abs(int(s[0]) - int(b[0])) + abs(int(s[1]) - int(b[1])))
        S.append(s)

    for x, y, d in S:
        for dx in range(d + 2):
            dy = (d + 1) - dx
            if no_coverage(x + dx, y + dy, S, target):
                return (y + dy) + (x + dx) * target
            if no_coverage(x - dx, y - dy, S, target):
                return (y - dy) + (x - dx) * target
            if no_coverage(x + dx, y - dy, S, target):
                return (y - dy) + (x + dx) * target
            if no_coverage(x - dx, y + dy, S, target):
                return (y + dy) + (x - dx) * target

    return


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
