day_counts = [0] * 9

fp =open("input.txt")
line = fp.read()
fp.close()

for v in line.strip().split(","):
    day_counts[int(v)] += 1

for _ in range(256):
    ready = day_counts.pop(0)
    day_counts.append(ready)
    day_counts[6] += ready

print(sum(day_counts))

