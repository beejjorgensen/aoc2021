INPUT = "input.txt"
#INPUT = "input1.txt"

production = {}

with open(INPUT) as fp:
	polymer = fp.readline().strip()
	fp.readline()

	for line in fp:
		src, dest = line.strip().split(" -> ")
		production[src] = dest
	
for _ in range(10):

	new_polymer = ""

	for i in range(len(polymer) - 1):
		pair = polymer[i:i+2]

		new_element = production[pair]

		new_polymer += f"{pair[0]}{new_element}"

	polymer = new_polymer + pair[1]

count = {}

for c in polymer:
	if c not in count:
		count[c] = 0

	count[c] += 1

"""
import math

max_count = -math.inf
min_count = math.inf

for c in count.values():
	if c > max_count:
		max_count = c
	if c < min_count:
		min_count = c
"""

d = sorted(list(count.items()), key=lambda x: x[1])
min_count = d[0][1]
max_count = d[-1][1]

print(max_count - min_count)

