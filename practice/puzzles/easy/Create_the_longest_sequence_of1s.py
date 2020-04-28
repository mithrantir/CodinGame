import sys
import math

b = input()

zero_pos = []
for i in range(len(b)):
    if b[i] == '0':
        zero_pos.append(i)

lz = len(zero_pos)

if lz<=1:
    print(len(b))
else:
    zero_pos.append(len(b))
    best = zero_pos[1]
    for i in range(1,lz):
        length = zero_pos[i+1]-zero_pos[i-1]-1
        if length>best:
            best = length

print(best)
