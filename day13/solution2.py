import math

#INPUT="input1.txt"   # 17
INPUT="input.txt"

points = set()

def fold(axis, value):
    # partition and remap
    folded_points = set()
    remove_points = set()

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
            remove_points.add(p)

    points.difference_update(remove_points)
    points.update(folded_points)

def print_data():
    minp = [math.inf, math.inf]
    maxp = [-math.inf, -math.inf]

    for p in points:
        minp[0] = min(minp[0], p[0])
        minp[1] = min(minp[1], p[1])
        maxp[0] = max(maxp[0], p[0])
        maxp[1] = max(maxp[1], p[1])

    origin = (-minp[0], -minp[1])
    width = maxp[0] - minp[0] + 1
    height = maxp[1] - minp[1] + 1

    bitmap = []

    for _ in range(height):
        row = ['.'] * width;
        bitmap.append(row)

    #print(minp, maxp)

    for p in points:
        x = p[0] + origin[0]
        y = p[1] + origin[1]

        bitmap[y][x] = "#"

    for r in bitmap:
        print("".join(r))

with open(INPUT) as fp:
    section = 0

    for line in fp:

        line = line.strip()

        if section == 0:
            if line == "":
                section = 1
            else:
                points.add(tuple(map(int, line.split(","))))

        else:
            axis, value = line.split()[2].split("=")
            value = int(value)
            fold(axis, value)


print_data()

