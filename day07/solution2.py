import statistics

fp = open("input1.txt")
data = list(map(int, fp.read().strip().split(",")))
fp.close()

print(f"mean: {statistics.mean(data)}")
print(f"median: {statistics.median(data)}")
mean = int(statistics.mean(data) + 0.5)
print(f"rounded mean: {mean}")

g = lambda n: n * (n + 1) / 2
f = lambda x: g(abs(mean - x))

total = sum([f(x) for x in data])

print(total)
