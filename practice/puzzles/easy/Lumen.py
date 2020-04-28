import sys
import math

n = int(input())

lumen = [[0 for i in range(n)] for j in range(n)]
l = int(input())
for i in range(n):
    line = input()
    for j in range(len(line)):
        if line[j] == 'C':
            x, y = i, j // 2
            for ii in range(n):
                for jj in range(n):
                    dx, dy = abs(ii - x), abs(jj - y)
                    if dx < l and dy < l:
                        lumen[ii][jj] = 1

ans = 0
for ii in lumen:
    for jj in ii:
        if jj == 0:
            ans += 1

print(ans)
