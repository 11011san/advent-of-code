import re
import aoc_lube
import networkx as nx

input = """30373
25512
65332
33549
35390""".splitlines()

day = 8
year = 2022


input = aoc_lube.fetch(year, day).splitlines()


def part1():
    map = [[x for x in y] for y in input]
    map_inv = list(zip(*map))
    lenX = len(map[0])
    lenY = len(map)
    count = lenX * 2 + lenY * 2 - 4
    for x in range(1, lenX - 1):
        for y in range(1, lenY - 1):
            height = map[y][x]
            if height > max(map[y][:x]):
                count += 1
                continue
            if height > max(map[y][x + 1:]):
                count += 1
                continue
            if height > max(map_inv[x][:y]):
                count += 1
                continue
            if height > max(map_inv[x][y + 1:]):
                count += 1
                continue
    return count


def reverse(param):
    param.reverse()
    return param


def part2():
    map = [[x for x in y] for y in input]
    map_inv = list(zip(*map))
    map_inv = [list(x) for x in map_inv]
    lenX = len(map[0])
    lenY = len(map)
    best = 0
    for x in range(1, lenX - 1):
        for y in range(1, lenY - 1):
            score = 1
            height = map[y][x]
            v = 0
            for t in reverse(map[y][:x]):
                v += 1
                if t >= height:
                    break
            score *= v
            v = 0
            for t in map[y][x + 1:]:
                v += 1
                if t >= height:
                    break
            score *= v
            v = 0
            for t in reverse(map_inv[x][:y]):
                v += 1
                if t >= height:
                    break
            score *= v
            v = 0
            for t in map_inv[x][y + 1:]:
                v += 1
                if t >= height:
                    break
            score *= v
            if score > best:
                best = score
    return best


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
