import sys
import math

width, height = [int(i) for i in input().split()]
maze = []
for i in range(height):
    maze.append([c for c in input()])

for n in range(height):
    for m in range(width):
        if maze[n][m] == '0':
            ans = 0
            if n > 0 and maze[n - 1][m] != '#': ans += 1
            if m > 0 and maze[n][m - 1] != '#': ans += 1
            if n < height - 1 and maze[n + 1][m] != '#': ans += 1
            if m < width - 1 and maze[n][m + 1] != '#': ans += 1
            maze[n][m] = str(ans)

for line in maze:
    print(''.join(c for c in line))
