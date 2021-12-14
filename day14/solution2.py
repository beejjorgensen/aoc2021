INPUT = "input.txt"
#INPUT = "input1.txt"

production = {}

with open(INPUT) as fp:
	polymer = fp.readline().strip()
	fp.readline()

	for line in fp:
		src, dest = line.strip().split(" -> ")
		production[src] = dest

pair_count = {}
element_count = {}

def add_pair(pair, pair_count_d, count=1):
	if pair not in pair_count_d:
		pair_count_d[pair] = 0

	pair_count_d[pair] += count

def add_element(element, count=1):
	if element not in element_count:
		element_count[element] = 0

	element_count[element] += count

for c in polymer:
	add_element(c)

for i in range(len(polymer) - 1):
	pair = polymer[i:i+2]
	add_pair(pair, pair_count)

for _ in range(40):
	new_pair_count = {}

	for pair, count in pair_count.items():
		new_element = production[pair]

		add_element(new_element, count)

		add_pair(pair[0] + new_element, new_pair_count, count)
		add_pair(new_element + pair[1], new_pair_count, count)

	pair_count = new_pair_count


d = sorted(list(element_count.items()), key=lambda x: x[1])
min_count = d[0][1]
max_count = d[-1][1]

print(max_count - min_count)
