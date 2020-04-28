import sys
import math


def is_inside_polygon(polygon, x, y):
    A = []
    B = []
    C = []
    for i in range(len(polygon)):
        p1x, p1y = polygon[i]
        p2x, p2y = polygon[(i + 1) % len(polygon)]

        a = -(p2y - p1y)
        b = p2x - p1x
        c = -(a * p1x + b * p1y)
        
        A.append(a)
        B.append(b)
        C.append(c)

    D = []
    for i in range(len(A)):
        d = A[i] * x + B[i] * y + C[i]
        D.append(d)

    t1 = all(d >= 0 for d in D)
    t2 = all(d <= 0 for d in D)
    return t1 or t2


n = int(input())
target = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    target.append((x, y))
m = int(input())
for i in range(m):
    x, y = [int(j) for j in input().split()]
    if is_inside_polygon(target, x, y):
        print("hit")
    else:
        print("miss")

