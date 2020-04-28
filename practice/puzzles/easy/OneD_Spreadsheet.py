import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

refer = 0


def value(arg):
    global refer
    if arg[0] == '$':
        refer += 1
        return [int(arg[1:])]
    else:
        return int(arg)


n = int(input())
noper = 0
ram = [[None] * n, [None] * n]
oper = [None] * n
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    if operation == "VALUE":
        ram[0][i] = value(arg_1)
    elif operation == "ADD":
        noper, oper[i] = noper + 1, 0
        ram[0][i], ram[1][i] = value(arg_1), value(arg_2)
    elif operation == "SUB":
        noper, oper[i] = noper + 1, 1
        ram[0][i], ram[1][i] = value(arg_1), value(arg_2)
    elif operation == "MULT":
        noper, oper[i] = noper + 1, 2
        ram[0][i], ram[1][i] = value(arg_1), value(arg_2)

while refer > 0:

    for i in range(n):
        if oper[i] is not None and type(ram[0][i]) == int and type(ram[1][i]) == int:
            noper = noper - 1
            if oper[i] == 0:
                ram[0][i] += ram[1][i]
            elif oper[i] == 1:
                ram[0][i] -= ram[1][i]
            else:
                ram[0][i] *= ram[1][i]
            oper[i] = None

    for i in range(n):
        for j in range(2):
            if type(ram[j][i]) == list:
                ref = ram[j][i][0]
                if type(ram[0][ref]) == int and oper[ref] is None:
                    ram[j][i] = ram[0][ref]
                    refer = refer - 1

while noper > 0:
    for i in range(n):
        if oper[i] is not None:
            noper = noper - 1
            if oper[i] == 0:
                ram[0][i] += ram[1][i]
            elif oper[i] == 1:
                ram[0][i] -= ram[1][i]
            else:
                ram[0][i] *= ram[1][i]
            oper[i] = None

for i in range(n):
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(ram[0][i])