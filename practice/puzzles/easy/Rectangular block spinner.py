import sys
import math


def rotate_by_90(b, dim):
    b_r = [[' ' for ii in range(dim)] for jj in range(dim)]
    for ii in range(dim):
        for jj in range(dim):
            b_r[ii][jj] = b[jj][dim - 1 - ii]
    return b_r


def rotate_by_45(b, dim):  # ugly
    b_r = [[] for ii in range(2 * dim - 1)]
    for ii in range(dim):
        for jj in range(ii + 1):
            b_r[ii].append(b[jj][dim - 1 - ii + jj])
    for ii in range(dim - 1):
        for jj in range(dim - 1 - ii):
            b_r[dim + ii].append(b[ii + 1 + jj][jj])
    b_r_print = [[] for ii in range(2 * dim - 1)]
    for ii in range(dim - 1):
        for jj in range(dim - 2 - ii):
            b_r_print[ii].append(' ')
        for jj in range(len(b_r[ii])):
            b_r_print[ii].append(' ')
            b_r_print[ii].append(b_r[ii][jj])
        for jj in range(dim - 1 - ii):
            b_r_print[ii].append(' ')
    b_r_print[dim - 1].append(b_r[dim - 1][0])
    for jj in range(1, len(b_r[dim - 1])):
        b_r_print[dim - 1].append(' ')
        b_r_print[dim - 1].append(b_r[dim - 1][jj])
    for ii in range(dim - 1):
        for jj in range(ii):
            b_r_print[dim + ii].append(' ')
        for jj in range(len(b_r[dim + ii])):
            b_r_print[dim + ii].append(' ')
            b_r_print[dim + ii].append(b_r[dim + ii][jj])
        for jj in range(ii + 1):
            b_r_print[dim + ii].append(' ')

    return b_r_print


size = int(input())
angle = int(input())
rotations = (angle // 45) % 8
right_rotations = rotations // 2

board = [[' ' for ii in range(size)] for jj in range(size)]
for i in range(size):
    line = input()
    for j in range(size):
        board[i][j] = line[2 * j]

for i in range(right_rotations):
    board = rotate_by_90(board, size)

b_rot = rotate_by_45(board, size)
for l in b_rot:
    print(''.join(c for c in l))
