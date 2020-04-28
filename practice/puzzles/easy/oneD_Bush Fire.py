import sys
import math


def calculate_drops(s):
    s_l, n, dr, ls = [c for c in s], 0, 0, len(s)
    while n < ls:
        while s_l[n] == '.':
            n += 1
            if n == ls:
                break
        if n == ls:
            break
        elif n >= ls-2:
            dr += 1
            break
        else:
            n, dr = n+3, dr+1
    return dr


n = int(input())
for i in range(n):
    line = input()
    print(calculate_drops(line))
