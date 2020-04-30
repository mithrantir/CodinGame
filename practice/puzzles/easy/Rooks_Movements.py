import sys
import math


def chess_to_cartesian(pos):
    return int(pos[1]) - 1, 7 - ord(pos[0]) + ord('a')


def cartesian_to_chess(x, y):
    return chr(ord('a') + 7 - y) + str(x + 1)


dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

board = [['.' for i in range(8)] for j in range(8)]
rook_position = input()
rx, ry = chess_to_cartesian(rook_position)
nb_pieces = int(input())
for i in range(nb_pieces):
    colour, one_piece = input().split()
    colour = int(colour)
    px, py = chess_to_cartesian(one_piece)
    board[px][py] = str(colour)

sol = []
prefix = "R" + rook_position
for d in dirs:
    tx, ty = rx + d[0], ry + d[1]
    while 0 <= tx < 8 and 0 <= ty < 8 and board[tx][ty] == '.':
        sol.append(prefix + "-" + cartesian_to_chess(tx, ty))
        tx, ty = tx + d[0], ty + d[1]
    if 0 <= tx < 8 and 0 <= ty < 8 and board[tx][ty] == '1':
        sol.append(prefix + "x" + cartesian_to_chess(tx, ty))

sol.sort()
for s in sol:
    print(s)