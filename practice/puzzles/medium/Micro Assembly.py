
a, b, c, d = [int(i) for i in input().split()]
reg = {'a': a, 'b': b, 'c': c, 'd': d}
n = int(input())
program = []
for i in range(n):
    program.append(input().split())

ind = 0
while ind < n:
    if program[ind][0] == 'MOV':
        if program[ind][2].isalpha():
            reg[program[ind][1]] = reg[program[ind][2]]
        else:
            reg[program[ind][1]] = int(program[ind][2])
    elif program[ind][0] == 'ADD':
        if program[ind][2].isalpha() and program[ind][3].isalpha():
            reg[program[ind][1]] = reg[program[ind][2]] + reg[program[ind][3]]
        elif program[ind][2].isalpha():
            reg[program[ind][1]] = reg[program[ind][2]] + int(program[ind][3])
        elif program[ind][3].isalpha():
            reg[program[ind][1]] = int(program[ind][2]) + reg[program[ind][3]]
        else:
            reg[program[ind][1]] = int(program[ind][2]) + int(program[ind][3])
    elif program[ind][0] == 'SUB':
        if program[ind][2].isalpha() and program[ind][3].isalpha():
            reg[program[ind][1]] = reg[program[ind][2]] - reg[program[ind][3]]
        elif program[ind][2].isalpha():
            reg[program[ind][1]] = reg[program[ind][2]] - int(program[ind][3])
        elif program[ind][3].isalpha():
            reg[program[ind][1]] = int(program[ind][2]) - reg[program[ind][3]]
        else:
            reg[program[ind][1]] = int(program[ind][2]) - int(program[ind][3])
    elif program[ind][0] == 'JNE':
        if program[ind][3].isalpha():
            if reg[program[ind][2]] != reg[program[ind][3]]:
                ind = int(program[ind][1]) - 1
        else:
            if reg[program[ind][2]] != int(program[ind][3]):
                ind = int(program[ind][1]) - 1
    ind += 1

print("{} {} {} {}".format(reg['a'], reg['b'], reg['c'], reg['d']))
