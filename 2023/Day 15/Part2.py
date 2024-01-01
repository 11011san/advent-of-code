import re

input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

input = open("input1.txt", "r").read().strip()

input = input.split(",")


def hash(value):
    result = 0
    for char in value:
        result = ((result + ord(char)) * 17) % 256
    return result


output = 0

boxes = [[] for _ in range(256)]

for part in input:
    split = re.match(r"^([a-z]+)([\-=\d]+)", part)
    label = split.group(1)
    box = hash(label)
    if split.group(2).startswith("="):
        found = False
        for i, lens in enumerate(boxes[box]):
            if lens[0] == label:
                found = True
                boxes[box][i] = ((label, int(split.group(2)[1:])))
        if not found:
            boxes[box].append((label, int(split.group(2)[1:])))
    else:
        for lens in boxes[box]:
            if lens[0] == label:
                boxes[box].remove(lens)
                break

for ib, box in enumerate(boxes):
    for li, lens in enumerate(box):
        output += (ib + 1) * (li + 1) * lens[1]
print(output)
