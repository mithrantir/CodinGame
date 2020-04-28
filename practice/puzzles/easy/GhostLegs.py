import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
hold = input().split()
game = hold.copy()
for i in range(h - 2):
    line = input()
    for i in range(w):
        if line[i] == '-' and i % 3 == 1:
            game[(i - 1) // 3], game[(i + 2) // 3] = game[(i + 2) // 3], game[(i - 1) // 3]

end = input().split()

for c in hold:
    print(c + end[game.index(c)])
