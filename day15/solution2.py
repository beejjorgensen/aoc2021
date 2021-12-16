import math
from minheap import MinHeap

#INPUT = "input1.txt"  # 315
INPUT = "input.txt"

orig_data = []

with open(INPUT) as fp:
    for line in fp:
        row = list(map(int, list(line.strip())))
        orig_data.append(row)

orig_data_height = len(orig_data)
orig_data_width = len(orig_data[0])

data_height = orig_data_height * 5
data_width = orig_data_width * 5

# Multiply data out

data = []

for r in range(data_height):
    sr = r % orig_data_height
    metar = r // orig_data_height

    row = []

    for c in range(data_width):
        sc = c % orig_data_width
        metac = c // orig_data_width

        addition = metar + metac

        new_value = orig_data[sr][sc] + addition
        if new_value > 9:
            new_value -= 9;

        row.append(new_value)

    data.append(row)

"""
for r in data:
    for c in r:
        print(c, end="")
    print()

import sys; sys.exit()
"""

def make_grid(e):
    grid = []
    for r in range(data_height):
        row = []
        for c in range(data_width):
            row.append(e)
        grid.append(row)
    return grid

dist = make_grid(math.inf)
prev = make_grid(None)

to_visit = MinHeap()
to_visit_set = set()

def get_unvisited_neighbors(r, c):
    neighbors = []

    if (r-1,c) in to_visit_set:
        neighbors.append((r-1, c))

    if (r,c-1) in to_visit_set:
        neighbors.append((r, c-1))

    if (r+1,c) in to_visit_set:
        neighbors.append((r+1, c))

    if (r,c+1) in to_visit_set:
        neighbors.append((r, c+1))

    return neighbors

fdist = lambda x: dist[x[0]][x[1]]

for r in range(data_height):
    for c in range(data_width):
        d = 0 if r == 0 and c == 0 else math.inf
        dist[r][c] = d
        to_visit_set.add((r, c))

to_visit.add((0,0), key=fdist)

while not to_visit.is_empty():
    r, c = to_visit.remove(key=fdist)

    if (r,c) not in to_visit_set:
        continue

    to_visit_set.remove((r, c))
    d = dist[r][c]
    #print(f">>> Visiting {r} {c}, {d}")

    for nr, nc in get_unvisited_neighbors(r, c):
        new_dist = d + data[nr][nc]
        #print(f"Neighbor {nr},{nc}, old={dist[nr][nc]}, new={new_dist}")
        if new_dist < dist[nr][nc]:
            dist[nr][nc] = new_dist
            prev[nr][nc] = (r, c)
            #print("Setting")

        if (nr,nc) in to_visit_set:
            to_visit.add((nr, nc), key=fdist)

"""
for r in prev:
    for c in r:
        print(f"{str(c):8}", end="")
    print()
"""

# Backtrack

r = data_height - 1
c = data_height - 1

total = 0

while prev[r][c] is not None:
    total += data[r][c]
    r, c = prev[r][c]

print(total)

