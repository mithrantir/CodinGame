import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h, count_x, count_y = [int(i) for i in input().split()]

x_dims, y_dims = [0], [0]
rect_x, rect_y = {}, {}
for i in input().split():
    x = int(i)
    for n in x_dims:
        if x - n in rect_x:
            rect_x[x - n] += 1
        else:
            rect_x[x - n] = 1
    x_dims.append(x)
for n in x_dims:
    if w - n in rect_x:
        rect_x[w - n] += 1
    else:
        rect_x[w - n] = 1

for i in input().split():
    y = int(i)
    for n in y_dims:
        if y - n in rect_y:
            rect_y[y - n] += 1
        else:
            rect_y[y - n] = 1
    y_dims.append(y)
for n in y_dims:
    if h - n in rect_y:
        rect_y[h - n] += 1
    else:
        rect_y[h - n] = 1

answer = 0
for key in rect_x:
    if key in rect_y:
        answer += rect_x[key] * rect_y[key]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(answer)