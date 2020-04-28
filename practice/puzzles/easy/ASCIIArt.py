import sys
import math

f = open("00000test.txt", "r").read().split('\n')
l = int(f[0])
h = int(f[1])
t = f[2]
# l = int(input())
# h = int(input())
# t = input()
letters = []
for i in range(h):
    letters.append(f[i+3])
    # letters.append(input())

for i in range(h):
    line = ""
    for c in t:
        if c.isalpha():
            pos = ord(c.lower()) - ord('a')
        else:
            pos = 26
        first = pos * l
        line += letters[i][first:first+l]
    print(line)
