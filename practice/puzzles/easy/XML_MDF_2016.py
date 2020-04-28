import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sequence = input()

weights = [0.]*26
tags = []
dash = False
for c in sequence:
    if dash:
        dash = False
        continue
    if c.isalpha(): 
        tags.append(c)
        weights[ord(c)-ord('a')] += 1/len(tags)
    else:
        tags.pop()
        dash = True

answer = chr(97+weights.index(max(weights)))
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(answer)
