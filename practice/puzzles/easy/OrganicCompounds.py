import sys
import math

compound = []


def check_carbon(line, pos):
    n_hydro = int(compound[line][pos+2])
    n_left, n_right, n_up, n_down = 0, 0, 0, 0
    if pos > 0 and compound[line][pos-1] == ')':
        n_left = int(compound[line][pos-2])
    if pos < len(compound[line])-3 and compound[line][pos+3] == '(':
        n_right = int(compound[line][pos + 4])
    if line > 0 and pos < len(compound[line-1])-1 and compound[line-1][pos] == '(':
        n_up = int(compound[line-1][pos+1])
    if line < n-1 and pos < len(compound[line+1])-1 and compound[line+1][pos] == '(':
        n_down = int(compound[line+1][pos+1])
    return n_hydro + n_left + n_right + n_up + n_down == 4


f = open("00000.txt", "r").read().split("\n")
n = int(f[0])

# n = int(input())
for i in range(n):
    # compound.append(input())
    compound.append(f[i+1])

valid = True
for i in range(n):
    for j in range(len(compound[i])):
        if compound[i][j] == 'C':
            valid = check_carbon(i, j)
            if not valid:
                break
    if not valid:
        break

if valid:
    print("VALID")
else:
    print("INVALID")