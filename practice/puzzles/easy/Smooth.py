import sys
import math

n = int(input())
for i in range(n):
    f = int(input())
    while f % 2 == 0:
        f = f // 2
    while f % 3 == 0:
        f = f // 3
    while f % 5 == 0:
        f = f // 5
    if f == 1:
        print("VICTORY")
    else:
        print("DEFEAT")
