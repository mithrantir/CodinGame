import sys
import math

x = int(input())
n = int(input())
bricks = []
for i in input().split():
    bricks.append(int(i))
bricks.sort(reverse=True)

h = 1
energy = 0
while len(bricks) >= x:
    energy += sum(bricks[:x]) * (h - 1) * 0.65
    bricks = bricks[x:]
    h = h + 1

energy += sum(bricks) * (h - 1) * 0.65
print("{:0.3f}".format(energy))