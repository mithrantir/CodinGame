import sys
import math


def digit_sum(n):
    return sum([int(c) for c in str(n)])


def next_item(n):
    return n+digit_sum(n)


r1 = int(input())
r2 = int(input())

while r1 != r2:
    if r1 < r2:
        r1 = next_item(r1)
    else:
        r2 = next_item(r2)

print(r1)
