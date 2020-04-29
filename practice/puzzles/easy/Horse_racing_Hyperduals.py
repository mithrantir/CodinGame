import sys
import math


def distance(h1, h2):
    return abs(h2[1]-h1[1])+abs(h2[0]-h1[0])


n = int(input())
horses =[]
for i in range(n):
    v, e = [int(j) for j in input().split()]
    horses.append([v,e])

horses.sort(key=lambda x: (x[0], x[1]))
dist = distance(horses[0], horses[-1])
for i in range(1, len(horses)):
    for j in range(i):
        temp = distance(horses[i], horses[j])
        if temp < dist:
            dist = temp

print(dist)