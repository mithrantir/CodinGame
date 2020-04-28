import sys
import math

n, m, c = [int(i) for i in input().split()]
power, status = [], []
for i in input().split():
    power.append(int(i))
    status.append(0)

fuse, maxfuse, blown = 0, 0, False
for i in input().split():
    mx = int(i)
    fuse -= power[mx - 1] * status[mx - 1]
    status[mx - 1] = (status[mx - 1] + 1) % 2
    fuse += power[mx - 1] * status[mx - 1]
    if fuse > c:
        blown = True
        break
    elif fuse > maxfuse:
        maxfuse = fuse

if blown:
    print("Fuse was blown.")
else:
    print("Fuse was not blown.")
    print("Maximal consumed current was {} A.".format(maxfuse))
