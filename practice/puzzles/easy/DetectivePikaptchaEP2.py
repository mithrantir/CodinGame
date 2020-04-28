import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lturn = [(0, 1), (-1, 0), (0, -1), (1, 0)]

width, height = (5, 3)
maze = [['>', '0', '0', '0', '#'], ['#', '0', '#', '0', '0'], ['0', '0', '#', '0', '#']]
side = 'L'


def next_step(posx, posy , dir, side):
    d = lturn.index(dir)
    if side == 'L': addn = 1
    else: addn = 3

    d = (d+addn)%4
    checkx, checky = posx + lturn[d][0], posy + lturn[d][1]
    while checkx<0 or checky<0 or checkx==height or checky==width or maze[checkx][checky] == "#":
        d = (d + addn + 2) % 4
        checkx, checky = posx + lturn[d][0], posy + lturn[d][1]

    maze[checkx][checky] = str(int(maze[checkx][checky]) + 1)
    return checkx, checky, lturn[d]


# width, height = [int(i) for i in input().split()]
# maze = []
# for i in range(height):
#     maze.append([c for c in input()])
# side = input()

stx, sty, d = 0, 0, (0, 0)
for n in range(height):
    for m in range(width):
        if maze[n][m] == '>':
            stx, sty, d = n, m, (0, 1)
            maze[n][m] = '0'
        elif maze[n][m] == '<':
            stx, sty, d = n, m, (0, -1)
            maze[n][m] = '0'
        elif maze[n][m] == '^':
            stx, sty, d = n, m, (-1, 0)
            maze[n][m] = '0'
        elif maze[n][m] == 'v':
            stx, sty, d = n, m, (1, 0)
            maze[n][m] = '0'

ans = 0
if stx > 0 and maze[stx - 1][sty] != '#': ans += 1
if sty > 0 and maze[stx][sty - 1] != '#': ans += 1
if stx < height - 1 and maze[stx + 1][sty] != '#': ans += 1
if sty < width - 1 and maze[stx][sty + 1] != '#': ans += 1

if ans>0:
    nx, ny, nd = next_step(stx, sty, d, side)
    while nx != stx or ny != sty:
        nx, ny, nd = next_step(nx, ny, nd, side)

for line in maze:
    print(''.join(c for c in line))
