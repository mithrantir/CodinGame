import sys
import math


def isValid(s):
    if not s[:-1].isnumeric() or (s[-1] == 'X' and len(s) != 10):
        return False
    s_l = [c for c in s]
    if s_l[-1] == 'X':
        s_l[-1] = "10"

    if len(s_l) == 10:
        sm = 0
        for i in range(10):
            sm += int(s_l[i]) * (10 - i)
        return sm % 11 == 0
    elif len(s_l) == 13:
        sm = 0
        for i in range(0,12,2):
            sm += int(s_l[i]) + 3*int(s_l[i+1])
        sm += int(s_l[12])
        return sm % 10 == 0
    else:
        return False


n = int(input())
isbn = []
for i in range(n):
    isbn.append(input())

invalid = []
for s in isbn:
    if not isValid(s):
        invalid.append(s)

print("{} invalid:".format(len(invalid)))
for s in invalid:
    print(s)
