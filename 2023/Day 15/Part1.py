
input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

input = open("input1.txt", "r").read().strip()

input = input.split(",")


def hash(value):
    result = 0
    for char in value:
        result = ((result + ord(char)) * 17) % 256
    return result


output = 0

for part in input:
    value = hash(part)
    print(f"\"{part}\"={value}")
    output += value

print(output)
