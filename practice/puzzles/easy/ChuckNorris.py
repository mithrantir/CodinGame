import sys
import math
from numpy import binary_repr

def encode_bin(s):
    ans = ""
    c, ind, ln = s[0], 0, len(s)
    while ind<len(s):
        if c == '1': ans += " 0 "
        else: ans += " 00 "
        count = 0
        while s[ind] == c:
            ind, count = ind+1, count+1
            if ind == len(s): break
        ans += count*'0'
        c = str((int(c) + 1) % 2)

    return ans


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

binary_str = ""
for c in message:
    binary_str += binary_repr(ord(c), width=7)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(encode_bin(binary_str)[1:])