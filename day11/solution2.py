INPUT = "input.txt"
#INPUT = "input1.txt"

ROW_COUNT = COL_COUNT = 10

data = []

with open(INPUT) as fp:
	for line in fp:
		row = list(map(int, list(line.strip())))
		data.append(row)

total_popped = 0
tens = set()
popped = set()

def reset_popped():
	for r, c in popped:
		data[r][c] = 0

def increment():
	for r in range(ROW_COUNT):
		for c in range(COL_COUNT):
			add_to_octopus(r, c)

def add_to_octopus(r, c):
	if r >= 0 and c >= 0 and r < ROW_COUNT and c < COL_COUNT:
		data[r][c] += 1
		if data[r][c] > 9:
			tens.add((r, c))
			popped.add((r, c))
			data[r][c] = -99999   # prevent popping again

def add_to_neighbors(r, c):
	add_to_octopus(r-1, c-1)
	add_to_octopus(r-1, c+0)
	add_to_octopus(r-1, c+1)

	add_to_octopus(r+0, c-1)
	add_to_octopus(r+0, c+1)

	add_to_octopus(r+1, c-1)
	add_to_octopus(r+1, c+0)
	add_to_octopus(r+1, c+1)

def process_tens():
	while len(tens) > 0:
		r, c = tens.pop()
		add_to_neighbors(r, c)

def print_data():
	for row in data:
		print("".join([str(x) for x in row]))

	print()

all_popped_step = None

step = 0

while all_popped_step is None:
	step += 1

	popped = set()

	increment()
	process_tens()

	popped_this_time = len(popped)

	if popped_this_time == 100:
		all_popped_step = step

	total_popped += popped_this_time

	reset_popped()

print(all_popped_step)
