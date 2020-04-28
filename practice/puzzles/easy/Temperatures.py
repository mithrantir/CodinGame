import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
# a temperature expressed as an integer ranging from -273 to 5526
if n == 0:
    ans = 0
else:
    ans = min(sorted([int(t) for t in input().split()], reverse=True), key=abs)
print(ans)
