import sys
import math

n = int(input())
cards = []
for i in input().split():
    cards.append(int(i))

cost = 0
while len(cards)>1:
    cards.sort()
    ncard = cards.pop(0) + cards.pop(0)
    cost += ncard
    cards.append(ncard)

print(cost)