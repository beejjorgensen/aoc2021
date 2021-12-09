import math

INPUT="input.txt"
#INPUT="input1.txt"

data = []

with open(INPUT) as fp:
    for line in fp:
        data.append(list(map(int, list(line.strip()))))

data_height = len(data)
data_width = len(data[0]) # assumes square data

def get_neighbors(row, col):
    neighbors = []

    neighbors.append(data[row][col-1] if col > 0 else math.inf)
    neighbors.append(data[row-1][col] if row > 0 else math.inf)
    neighbors.append(data[row][col+1] if col < data_width - 1 else math.inf)
    neighbors.append(data[row+1][col] if row < data_height - 1 else math.inf)

    return neighbors

total_risk_level = 0

for row in range(data_height):
    for col in range(data_width):

        val = data[row][col]
        neighbors = get_neighbors(row, col)

        if val < min(neighbors):
            risk_level = 1 + val
            total_risk_level += risk_level

print(total_risk_level)



