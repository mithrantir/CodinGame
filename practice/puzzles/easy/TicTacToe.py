import sys
import math


def win_pos(b):
    if b[0][0] == b[0][1] == b[0][2] == 'O':
        return True
    if b[0][0] == b[1][1] == b[2][2] == 'O':
        return True
    if b[0][0] == b[1][0] == b[2][0] == 'O':
        return True
    if b[1][0] == b[1][1] == b[1][2] == 'O':
        return True
    if b[2][0] == b[2][1] == b[2][2] == 'O':
        return True
    if b[0][1] == b[1][1] == b[2][1] == 'O':
        return True
    if b[0][2] == b[1][2] == b[2][2] == 'O':
        return True
    if b[0][2] == b[1][1] == b[2][0] == 'O':
        return True
    return False


board = [[], [], []]

for i in range(3):
    line = input()
    for c in line:
        board[i].append(c)

can_win = False
for i in range(3):
    for j in range(3):
        if board[i][j] == '.':
            board[i][j] = 'O'
            can_win = win_pos(board)
            if can_win:
                break
            board[i][j] = '.'
    if can_win:
        break

if can_win:
    for i in range(3):
        print("".join(c for c in board[i]))
else:
    print("false")