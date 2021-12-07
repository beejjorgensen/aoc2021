day_counts = [0] * 8

fp =open("input1.txt")
line = fp.read()
fp.close()

for v in line.strip().split(","):
    day_counts[int(v)] += 1


