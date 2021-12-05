WINDOW_SIZE = 3
data = []

with open("input.txt") as fp:
    for line in fp:
        data.append(int(line))

count = 0
prev = None

for i in range(len(data) - WINDOW_SIZE + 1):
    cur = sum(data[i:i + WINDOW_SIZE])
    if prev is not None and cur > prev:
        count += 1

    prev = cur

print(count)

#22469
