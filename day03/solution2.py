data = []

with open("input.txt") as fp:
    counts = None

    for line in fp:
        line = line.strip()

        data.append(line)

        if counts is None:
            counts = [0] * len(line)

        for i, v in enumerate(line):
            counts[i] += 1 if v == "1" else -1

def get_most_common(data, pos):
    count = 0

    for d in data:
        count += 1 if d[pos] == "1" else -1

    return "1" if count >= 0 else "0"

def process(data, mode):
    pos = 0
    result = data

    while len(result) > 1:
        assert(pos < len(result[0]))
        common = get_most_common(result, pos)
        new_result = []
        for d in result:
            if mode == "o2":
                if d[pos] == common:
                    new_result.append(d)
            else:
                if d[pos] != common:
                    new_result.append(d)

        result = list(new_result)
        pos += 1

    return result[0]

o2 = int(process(data, "o2"), 2)
co2 = int(process(data, "co2"), 2)

print(o2 * co2)

