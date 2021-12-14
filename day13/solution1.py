INPUT="input1.txt"   # 17
#INPUT="input.txt"

points = set()

def fold(axis, value):
    # partition and remap
    folded_points = set()

    if axis == "x":
        cmp_index = 0
    else:
        cmp_index = 1

    for p in points:
        if p[cmp_index] > value:
            # remap
            mp = list(p)
            mp[cmp_index] = 2 * value - mp[cmp_index]
            folded_points.add(tuple(mp))
            points.remove(p)

    points.update(folded_points)


with open(INPUT) as fp:
    section = 0

    for line in fp:

        line = line.strip()

        if section == 0:
            if line == "":
                section = 1
            else:
                points.add(tuple(line.split(",")))

        else:
            axis, value = line.split()[2].split("=")
            fold(axis, value)
            break

print(points)
print(len(points))

