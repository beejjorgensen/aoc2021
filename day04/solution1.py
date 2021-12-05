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
            board.append(list(map(int, line.split())))

    
    if board != []:
        boards.append(board)

def add_move(board, m):

def test_win(b):
    
def move_boards(m):
    for board in boards:
        add_move(board, m)
        winner, win_sum = test_win(board)

        if winner:
            return board, win_sum

    return None, -1 

winning_board = None
i = 0

while winning_board is None and i < len(moves):
    winning_board, win_sum = move_boards(moves[i])
    if winning_board is not None: winning_move = moves[i]
    i += 1
    
assert(winning_board is not None)

board_total = sum(map(sum, winning_board))

unmarked_sum = board_total - win_sum

print(unmarked_sum * winning_move)


