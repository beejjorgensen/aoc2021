import statistics

fp = open("input.txt")
data = list(map(int, fp.read().strip().split(",")))
fp.close()

median = int(statistics.median(data))

#print(median)

total = sum([abs(median - x) for x in data])

print(total)
