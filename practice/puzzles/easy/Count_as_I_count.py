import sys
import math


ans = [0 for c in range(100)]

for i1 in range(1,13):
    ans[i1] += 1
    for i2 in range(1,13):
        ans[i1+i2] += 1
        for i3 in range(1,13):
            ans[i1+i2+i3] += 1
            for i4 in range(1,13):
                ans[i1+i2+i3+i4] += 1

for i1 in range(2,13):
    ans[i1] += 1
    for i2 in range(2,13):
        ans[i1+i2] += 1
        for i3 in range(2,13):
            ans[i1+i2+i3] += 1
            for i4 in range(2,13):
                ans[i1+i2+i3+i4] += 1

for i1 in range(2,13):
    for i2 in range(1,13):
        ans[i1+i2] += 2
        for i3 in range(1,13):
            ans[i1+i2+i3] += 3
            for i4 in range(1,13):
                ans[i1+i2+i3+i4] += 4

for i1 in range(2,13):
    for i2 in range(2,13):
        for i3 in range(1,13):
            ans[i1+i2+i3] += 3
            for i4 in range(1,13):
                ans[i1+i2+i3+i4] += 6

for i1 in range(2,13):
    for i2 in range(2,13):
        for i3 in range(2,13):
            for i4 in range(1,13):
                ans[i1+i2+i3+i4] += 4

n = int(input())
print(ans[50-n])