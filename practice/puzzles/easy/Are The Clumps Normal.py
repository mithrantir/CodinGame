import sys
import math

n = input()
n_digits = [int(c) for c in n]

normal, pr_clumbs = True, 1
for base in range(2, 10):
    clumbs , ind = 1, 0
    while ind+1 < len(n_digits):
        if n_digits[ind] % base != n_digits[ind+1] % base:
            clumbs += 1
        ind += 1
    if clumbs < pr_clumbs:
        normal = False
        break
    else:
        pr_clumbs = clumbs

if normal:
    print("Normal")
else:
    print(base)
