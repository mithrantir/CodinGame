import sys
import math


l = int(input())
n = int(input())
interval = []
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    interval.append([st,ed])

interval.sort()
answer = [interval[0]]

for inter in interval:
    xn, yn = inter[0], inter[1]
    xo, yo = answer[-1][0], answer[-1][1]
    if xn <= yo and yn >= yo:
        answer[-1][1] = yn
    elif xn > yo:
        answer.append([xn,yn])

if answer[0][0]==0 and answer[0][1]==l:
    print("All painted")
else:
    start = 0
    for x, y in answer:
        if x>start:
            print("{} {}".format(start,x))
        start = y
    if start < l:
        print("{} {}".format(start,l))
