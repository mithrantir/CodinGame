import sys
import math


def abs_val(r,i):
    return (r**2+i**2)**(1/2)


c = input()
ind = 1
while c[ind] != '+' and c[ind] != '-':
    ind += 1
rec = float(c[:ind])
imc = float(c[ind:-1])


def next_iter(x, y):
    return x**2 - y**2 + rec, 2*x*y + imc


m = int(input())
x, y, it = 0, 0, 0
while it < m and abs_val(x, y) <= 2:
    x, y = next_iter(x, y)
    it += 1

print(it)
