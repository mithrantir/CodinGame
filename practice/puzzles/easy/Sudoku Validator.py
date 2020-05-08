def check_rows_and_cols(board):
    for i in range(9):
        br, bc = set(), set()
        for j in range(9):
            br.add(board[i][j])
            bc.add(board[j][i])
        if len(br)<9 or len(bc)<9:
            return False
    return True


def check_blocks(board):
    for i in range(0,9,3):
        for j in range(0,9,3):
            b = set()
            for k in range(3):
                for l in range(3):
                    b.add(board[i+k][j+l])
            if len(b)<9:
                return False
    return True


board = []
for i in range(9):
    board.append([int(c) for c in input().split()])

valid = check_rows_and_cols(board) and check_blocks(board)
if valid:
    print("true")
else:
    print("false")
