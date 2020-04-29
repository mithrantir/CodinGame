import sys
import math


rotation_rule = { 'F': {'x':'U', 'x\'':'D', 'y':'L', 'y\'':'R', 'z':'F', 'z\'':'F' },
                  'B': {'x':'D', 'x\'':'U', 'y':'R', 'y\'':'L', 'z':'B', 'z\'':'B' },
                  'U': {'x':'B', 'x\'':'F', 'y':'U', 'y\'':'U', 'z':'R', 'z\'':'L' },
                  'D': {'x':'F', 'x\'':'B', 'y':'D', 'y\'':'D', 'z':'L', 'z\'':'R' },
                  'L': {'x':'L', 'x\'':'L', 'y':'B', 'y\'':'F', 'z':'U', 'z\'':'D' },
                  'R': {'x':'R', 'x\'':'R', 'y':'F', 'y\'':'B', 'z':'D', 'z\'':'U' }}

rotations = input().split()
f1, f2 = input(), input()
for r in rotations:
    f1, f2 = rotation_rule[f1][r], rotation_rule[f2][r]

print(f1+"\n"+f2)