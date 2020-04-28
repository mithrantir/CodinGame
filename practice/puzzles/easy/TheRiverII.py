import sys
import math


def digit_sum(n):
    return sum([int(c) for c in str(n)])


def next_item(n):
    return n + digit_sum(n)


def check(n):
    if n < 10 and n % 2 == 1:
        return False
    ln = len(str(n))
    st = max(5, n-9*ln)
    for k in range(st, n):
        if next_item(k) == n:
            return True
    return False


r = int(input())
if check(r):
    print("YES")
else:
    print("NO")
