#INPUT = "example_10.txt"   # 36 output
#INPUT = "example_19.txt"   # 103 output
#INPUT = "example_226.txt"  # 3509 output
INPUT = "input.txt"

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

def dup_small_count(path):
	count = {}

	for n in path:
		if n.islower():
			if n not in count:
				count[n] = 0
			count[n] += 1

	dup_count = 0

	for v in count.values():
		if v > 1:
			dup_count += 1

	return dup_count

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
			add_path = n.islower() \
					   and (n not in path or dup_small_count(path) == 0) \
					   and n != "start" \
					   or (n == "end" and "end" not in path) \
					   or n.isupper()


			if add_path:
				new_path = path + [n]
				to_visit.append(new_path)

print(total)


