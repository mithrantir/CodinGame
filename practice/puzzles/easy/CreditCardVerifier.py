import sys
import math


def is_valid(s):
    sme, smo = 0, 0
    for i in range(16):
        if i % 2 == 0:
            temp = int(s[i])*2
            if temp >= 10:
                temp -= 9
            sme += temp
        else:
            smo += int(s[i])
    return (smo+sme) % 10 == 0


n = int(input())
for i in range(n):
    card = "".join(c for c in input().split())
    if is_valid(card):
        print("YES")
    else:
        print("NO")

