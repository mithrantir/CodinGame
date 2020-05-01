import sys
import math


def dart_value(d, m):
    if d.isnumeric():
        return int(d)
    elif d == 'X':
        if m == 1: return -30
        else: return -20
    else:
        pos = d.index('*')
        return int(d[:pos]) * int(d[pos+1:])


n = int(input())
scoreOf, shootsOf, player = {}, {}, []
for i in range(n):
    p = input()
    scoreOf[p] = 0
    player.append(p)

for i in range(n):
    shootsOf[player[i]] = input().split()

turn, winner = -1, -1
while winner == -1:
    turn = (turn + 1) % n
    missed, score = 0, 0
    for i in range(3):
        dart = shootsOf[player[turn]].pop(0)
        score += dart_value(dart, missed)
        if dart == 'X':
            missed = 1
        else:
            missed = 0
        if scoreOf[player[turn]] + score == 101:
            winner = turn
            break
        elif scoreOf[player[turn]] + score > 101:
            break
    else:
        if score < -50:
            scoreOf[player[turn]] = 0
        else:
            scoreOf[player[turn]] += score

print(player[winner])
