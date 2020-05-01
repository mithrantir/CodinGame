import sys
import math

def is_on_line(ax, ay, a, b, c):
    return a * ax + b * ay + c == 0

def gcd(a,b):
    while b>0:
        a, b = b, a % b
    return a

x_a, y_a, x_b, y_b = [int(i) for i in input().split()]
n = int(input())
line_intersect = {}
online = False
for i in range(n):
    a, b, c = [int(j) for j in input().split()]
    if a<0:
        a, b, c = -a, -b, -c
    if is_on_line(x_a,y_a,a,b,c) or is_on_line(x_b,y_b,a,b,c):
        online = True
        break
    d = gcd(gcd(a, abs(b)), abs(c))
    a, b, c = a//d,  b//d, c//d
    if (a,b,c) not in line_intersect:
        num, den = -a*x_a-b*y_a-c, a*(x_b-x_a)+b*(y_b-y_a)
        if int(math.floor(num/den))==0:
            line_intersect[(a,b,c)] = 1
        else:
            line_intersect[(a,b,c)] = 0

if online:
    print("ON A LINE")
else:
    ans = 0
    for line in line_intersect:
        ans += line_intersect[line]
    if ans%2 == 1:
        print("NO")
    else:
        print("YES")
