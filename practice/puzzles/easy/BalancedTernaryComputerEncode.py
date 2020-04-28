import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

ans = ""
if n == 0: ans += "0"
while n != 0:
    res = (n+999999) % 3
    if res == 2: res = -1
    n = (n - res) // 3
    if res == -1: ans += 'T'
    elif res == 0: ans += "0"
    else: ans += "1"

print(ans[-1:-len(ans)-1:-1])