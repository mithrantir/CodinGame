import sys
import math

n = int(input())
for i1 in range(1+n//5):
    for i2 in range(1+i1):
        for i3 in range(1+n//3):
            if 5*i1+2*i2+3*i3 == n:
                print("{} {} {}".format(i1, i2, i3))
