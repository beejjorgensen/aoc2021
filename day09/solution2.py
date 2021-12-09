INPUT="input.txt"
#INPUT="input1.txt"

data = []

with open(INPUT) as fp:
    for line in fp:
        data.append(list(map(int, list(line.strip()))))

data_height = len(data)
data_width = len(data[0]) # assumes square data

visited = set()

def fill(row, col):
    to_visit = []
    rc = (row, col)

    to_visit.append(rc)
    size = 0

    while to_visit != []:
        r, c = to_visit.pop()
        if (r, c) in visited or r < 0 or r >= data_height \
                or c < 0 or c >= data_width or data[r][c] == 9:
            continue

        visited.add((r, c))
        size += 1

        to_visit.append((r-1, c))
        to_visit.append((r, c-1))
        to_visit.append((r+1, c))
        to_visit.append((r, c+1))

    return size

sizes = []

for row in range(data_height):
    for col in range(data_width):
        size = fill(row, col)

        if size != 0:
            sizes.append(size)

sizes.sort(reverse=True)

print(sizes[0] * sizes[1] * sizes[2])

for r in range(data_height):
    for c in range(data_width):
        if (r,c) in visited:
            print(".", end="")
        else:
            print("9", end="")
    print()



