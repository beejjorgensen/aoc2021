prev = None
count = 0

with open("input.txt") as fp:
    for line in fp:
        cur = int(line)
        if prev is not None and cur > prev:
            count += 1
        prev = cur

print(count)



