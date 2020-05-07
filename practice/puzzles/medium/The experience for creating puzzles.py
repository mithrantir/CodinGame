import math


def exp_level(lev):
    return int(math.floor( lev**(3/2) * 10 + 0.000001))


level = int(input())
xp = int(input())
n = int(input())
need, exper = xp, 300 * n
while exper >= need:
    level += 1
    exper -= need
    need = exp_level(level)

print(level)
print(need-exper)
