import sys
import math


w = int(input())
h = int(input())
tmap = []
for i in range(h):
    tmap.append([])
    for j in input().split():
        tmap[i].append(int(j))

tr_x, tr_y = -1, -1
for i in range(h):
    for j in range(w):
        if tmap[i][j] == 1:
            continue
        cells, valid = 0, 0
        if i>0 and j>0:
            cells, valid = cells + tmap[i-1][j-1], valid + 1
        if i>0:
            cells, valid = cells + tmap[i-1][j], valid + 1
        if i>0 and j<w-1:
            cells, valid = cells + tmap[i-1][j+1], valid + 1
        if j<w-1:
            cells, valid = cells + tmap[i][j+1], valid + 1
        if i<h-1 and j<w-1:
            cells, valid = cells + tmap[i+1][j+1], valid + 1
        if i<h-1:
            cells, valid = cells + tmap[i+1][j], valid + 1
        if i<h-1 and j>0:
            cells, valid = cells + tmap[i+1][j-1], valid + 1
        if j>0:
            cells, valid = cells + tmap[i][j-1], valid + 1
        if cells == valid:
            tr_x, tr_y = i, j
            break
    if tr_x != -1:
        break

print("{} {}".format(tr_y, tr_x))