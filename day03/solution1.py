with open("input.txt") as fp:
    counts = None

    for line in fp:
        line = line.strip()

        if counts is None:
            counts = [0] * len(line)

        for i, v in enumerate(line):
            counts[i] += 1 if v == "1" else -1

gamma = 0

for c in counts:
    assert(c != 0)
    gamma <<= 1
    gamma |= 1 if c > 0 else 0

mask = 2**(len(counts)) - 1

epsilon = ~gamma & mask

print(gamma * epsilon)
