import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def winner(n1, s1, n2, s2):
    rules = {'R': ['L', 'C'], 'P': ['R', 'S'], 'C': ['P', 'L'], 'L': ['S', 'P'], 'S': ['C', 'R']}
    if s2 in rules[s1]:
        return n1, s1
    elif s1 in rules[s2]:
        return n2, s2
    elif n1 < n2:
        return n1, s1
    else:
        return n2, s2


n = int(input())
tourn = []
pairing = {}
for i in range(n):
    numplayer, signplayer = input().split()
    numplayer = int(numplayer)
    tourn.append([numplayer, signplayer])
    pairing[i + 1] = []

while n > 1:
    for i in range(n // 2):
        pairing[tourn[i][0]].append(tourn[i + 1][0])
        pairing[tourn[i + 1][0]].append(tourn[i][0])
        nw, sw = winner(tourn[i][0], tourn[i][1], tourn[i + 1][0], tourn[i + 1][1])
        tourn[i][0], tourn[i][1] = nw, sw
        tourn.pop(i + 1)
    n = len(tourn)

print(tourn[0][0])
ans = ""
for n in pairing[tourn[0][0]]:
    ans += " " + str(n)
print(ans[1:])
