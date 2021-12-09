"""
1: 2  1x
7: 3  1x
4: 4  1x
2: 5  3x
3: 5
5: 5
6: 6  3x
0: 6
9: 6
8: 7  1x
"""

INPUT="input.txt"
#INPUT="input1.txt"
#INPUT="input2.txt"

def process(inp, out):
    count = 0

    iomap = {}

    for i in inp:
        l = len(i)
        key = "".join(sorted(i))
        if l == 2:
            iomap[key] = 1
        elif l == 3:
            iomap[key] = 7
        elif l == 4:
            iomap[key] = 4
        elif l == 7:
            iomap[key] = 8
        else:
            iomap[key] = None

    for o in out:
        key = "".join(sorted(o))
        if iomap[key] in [1, 7, 4, 8]:
            count += 1

    return count

total_count = 0

with open(INPUT) as fp:
    for line in fp:

        inp, out = line.split("|")

        inp = inp.strip().split()
        out = out.strip().split()

        total_count += process(inp, out)

print(total_count)
