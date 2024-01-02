import re
import aoc_lube
import networkx as nx
import operator

input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

day = 7
year = 2022
input = aoc_lube.fetch(year, day).splitlines()


class Dir:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.dir = []
        self.size = 0
        self.parent = None

    def add_file(self, file):
        self.size += file[1]
        self.files.append(file)
        if self.parent != None:
            self.parent.add_to_size(file[1])

    def add_to_size(self, amount):
        self.size += amount
        if self.parent != None:
            self.parent.add_to_size(amount)

    def add_dir(self, child):
        child.parent = self
        self.dir.append(child)
        self.size += child.size
        return child

    def getDir(self, name):
        for dir in self.dir:
            if dir.name == name:
                return dir
        return self.add_dir(Dir(name))

    def part1(self):
        ans = 0 if self.size > 100000 else self.size
        for dir in self.dir:
            ans += dir.part1()
        return ans

    def part2(self):
        list = [self]
        for dir in self.dir:
            list += dir.part2()
        return list


def build():
    global input
    root = Dir("/")
    current = root
    for row in input:
        if row.startswith("$ "):
            if row.startswith("$ cd .."):
                current = current.parent
            elif row.startswith("$ cd "):
                current = current.getDir(row[5:])
        elif row.startswith("dir "):
            current.add_dir(Dir(row[4:]))
        else:
            size, name = row.split(" ")
            current.add_file((name, int(size)))
    return root


def part1():
    return build().part1()


def part2():
    root = build()
    total = 70000000
    target = 30000000 - (70000000 - root.size)
    all = root.part2()
    all.sort(key=operator.attrgetter('size'))
    for dir in all:
        if dir.size > target:
            return dir.size
    return


aoc_lube.submit(year=year, day=day, part=1, solution=part1)

print('-------')
aoc_lube.submit(year=year, day=day, part=2, solution=part2)
