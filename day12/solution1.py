#INPUT = "example_10.txt"
#INPUT = "example_19.txt"
INPUT = "example_226.txt"
#INPUT = "input.txt"

links = {}   # map node to link sets

with open(INPUT) as fp:
	for line in fp:
		s, d = line.strip().split('-');

		if s not in links:
			links[s] = set()

		if d not in links:
			links[d] = set()

		links[s].add(d)
		links[d].add(s)

#print(links)

to_visit = [ ["start"] ]

total = 0

while to_visit != []:
	path = to_visit.pop()
	this_node = path[-1]

	if this_node == "end":
		#print(path)
		total += 1

	else:
		for n in links[this_node]:
			if n.islower() and n not in path or n.isupper():
				new_path = path + [n]
				to_visit.append(new_path)

print(total)


