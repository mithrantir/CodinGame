import sys
import math

last_seen = {}
a0 = int(input())
n = int(input())-1

ind, apr = 0, a0
while ind < n:
    ind += 1
    if apr in last_seen:
        a = ind - 1 - last_seen[apr]
        last_seen[apr] = ind-1
    else:
        last_seen[apr] = ind-1
        a = 0
    apr = a

print(apr)