sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

board = []

for i in range(1000):
	board.append([0] * 1000)

def draw_line(x0, y0, x1, y1):
	if x1 < x0:
		x0, x1 = x1, x0
		y0, y1 = y1, y0

	if y0 < y1:
		ystep = 1
	else:
		ystep = -1
	
	if x0 == x1:
		for y in range(y0, y1 + ystep, ystep):
			board[y][x0] += 1
	elif y0 == y1:
		for x in range(x0, x1 + 1):
			board[y0][x] += 1
	else:
		ycur = y0
		for x in range(x0, x1 + 1):
			board[ycur][x] += 1
			ycur += ystep

def count_highs():
	high_count = 0

	for y in range(len(board)):
		for x in range(len(board[y])):
			if board[y][x] > 1:
				high_count += 1

	return high_count


with open("input.txt") as fp:
	for line in fp:
		c0, _, c1 = line.split()
		x0, y0 = map(int, c0.split(","))
		x1, y1 = map(int, c1.split(","))

		draw_line(x0, y0, x1, y1)

c = count_highs()

"""
for row in range(10):
	for col in range(10):
		v = board[row][col]
		if v == 0: print(".", end="")
		else: print(v, end="")
	print()
"""

print(c)


