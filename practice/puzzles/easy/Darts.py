import sys
import math


import sys
import math


def calculate_score(x, y, a):
    if -a <= 2*x+2*y <= a and -a <= 2*x-2*y <= a:
        return 15
    elif 4*x*x + 4*y*y <= a*a:
        return 10
    elif -a <= 2*x <= a and -a <= 2*y <= a:
        return 5
    else:
        return 0


score = {}
size = int(input())
n = int(input())
for i in range(n):
    name = input()
    score[name] = 0
t = int(input())
for i in range(t):
    throw_name, throw_x, throw_y = input().split()
    throw_x = int(throw_x)
    throw_y = int(throw_y)
    score[throw_name] += calculate_score(throw_x, throw_y, size)

score_sorted = sorted(score.items(), key=lambda x: x[1], reverse = True)
for k, v in score_sorted:
    print("{} {}".format(k, v))
