import sys
import math

def crack_time(c, n):
    return (10 ** n) * 5 ** (c - n)


r = int(input())
v = int(input())
vault = []
for i in range(v):
    c, n = [int(j) for j in input().split()]
    vault.append(crack_time(c, n))

robber = []
for i in range(r):
    robber.append(vault.pop(0))

total = 0
while len(vault) > 0:
    fin = min(robber)
    total += fin
    for i in range(r):
        robber[i] -= fin
        if robber[i] == 0:
            robber[i] = vault.pop(0)

total += max(robber)
print(total)