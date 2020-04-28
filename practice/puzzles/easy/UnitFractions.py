import sys
import math

n = int(input())

sol = []
for x in range(n + 1, 2 * n):
    if n * x % (x - n) == 0:
        y = n * x // (x - n)
        sol.append([y, x])
sol.append([2 * n, 2 * n])

for y, x in sol:
    print("1/{} = 1/{} + 1/{}".format(n, y, x))
