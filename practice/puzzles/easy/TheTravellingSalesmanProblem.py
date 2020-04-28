import sys
import math

n = int(input())
cities = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    cities.append([x, y])

distance = 0
sx, sy = cities.pop(0)
cx, cy = sx, sy
while len(cities) > 0:
    nx, ny, nd, ind = 0, 0, 200, 0
    for i in range(len(cities)):
        x, y = cities[i]
        d = ((cx - x) ** 2 + (cy - y) ** 2) ** (1 / 2)
        if d < nd:
            nx, ny, nd, ind = x, y, d, i
    distance += nd
    cx, cy = cities.pop(ind)

distance += ((cx - sx) ** 2 + (cy - sy) ** 2) ** (1 / 2)
distance = int(math.floor(distance + 0.5))
print(distance)