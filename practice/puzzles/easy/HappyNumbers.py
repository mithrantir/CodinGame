import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def next_iter(n):
    return sum([int(c) ** 2 for c in str(n)])


def ishappy(n):
    orbit = {n}

    while n != 1:
        n = next_iter(n)
        if n in orbit: return False
        orbit.add(n)
    return True


n = int(input())
for i in range(n):
    x = input()
    if ishappy(x):
        print("{} :)".format(x))
    else:
        print("{} :(".format(x))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
