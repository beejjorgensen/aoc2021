boards = []
moves = None
board = None

with open("input.txt") as fp:

    for line in fp:
        line = line.strip()

        if line == '':
            if board is not None:
                boards.append(board)
            board = []
            continue

        if moves is None:
            moves = list(map(int, line.split(",")))

        else:
            board.append(list(map(lambda x: [int(x), False], line.split())))

    
    if board != []:
        boards.append(board)

def add_move(board, m):
	for row in range(5):
		for col in range(5):
			entry = board[row][col]
			if entry[0] == m:
				entry[1] = True

def test_win(b):
	def test_row(n):
		s = 0
		for entry in b[n]:
			if entry[1] == False:
				return None
			s += entry[0]
		return s

	def test_col(n):
		s = 0
		for row in b:
			entry = row[n]
			if entry[1] == False:
				return None
			s += entry[0]
		return s

	for i in range(5):
		s = test_row(i)
		if s is not None:
			return True, s

		s = test_col(i)
		if s is not None:
			return True, s

	return False, None

def move_boards(m):
    for board in boards:
        add_move(board, m)
        winner, win_sum = test_win(board)

        if winner:
            return board, win_sum

    return None, -1 

def get_board_total(b):
	t = 0

	for r in b:
		for c in r:
			if c[1] == False:
				t += c[0]

	return t

winning_board = None
i = 0

while winning_board is None and i < len(moves):
    winning_board, win_sum = move_boards(moves[i])
    if winning_board is not None: winning_move = moves[i]
    i += 1
    
assert(winning_board is not None)

for r in winning_board:
	print(r)

unmarked_sum = get_board_total(winning_board)

print(unmarked_sum * winning_move)


