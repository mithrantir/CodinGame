import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

turn = [(0,1),(1,0),(0,-1),(-1,0)]


def next_move(x, y, d):
    i = turn.index(d)
    chx, chy = x + turn[i][0], y + turn[i][1]
    nx, ny = chx + turn[i][0], chy + turn[i][1]
    while nx < 0 or ny < 0 or nx == height or ny == width or arena[nx][ny] == '#':
        i = (i + 1) % 4
        nx, ny = chx + turn[i][0], chy + turn[i][1]
    return chx, chy, turn[i]


# width, height = [int(i) for i in input().split()]
# n = int(input())
# arena = []
# for i in range(height):
#     arena.append([c for c in input()])

f = open('00000.txt', 'r').read().split('\n')
width, height = [int(c) for c in f[0].split()]
n = int(f[1])
arena = []
for i in range(height):
    arena.append([c for c in f[2+i]])

for i in range(height):
    for j in range(width):
        if arena[i][j] == 'O':
            x, y = i, j

nmoves = {}
i, step = 2, 0
nx, ny = x + turn[i][0], y + turn[i][1]
while nx < 0 or ny < 0 or nx == height or ny == width or arena[nx][ny] == '#':
    i = (i + 1) % 4
    nx, ny = x + turn[i][0], y + turn[i][1]
d = turn[i]

while (x, y, d) not in nmoves:
    nmoves[(x, y, d)] = step
    x, y, d = next_move(x, y, d)
    step += 1

x, y, d = [k for (k, v) in nmoves.items() if v == n % step][0]

print("{} {}".format(y, x))