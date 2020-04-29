import sys
import math

n = int(input())

xthen_commands = input().split(';')
command = []
for i in range(1,len(xthen_commands)):
    for j in range(int(xthen_commands[i][:len(xthen_commands[i])-1])):
        command.append(xthen_commands[i][-1])

roadpattern = []
for i in range(n):
    rthen = input().split(';')
    for i in range(int(rthen[0])):
        roadpattern.append([c for c in rthen[1]])

n = len(roadpattern)
pos = int(xthen_commands[0])-1
for i in range(n):
    if command[i] == 'R':
        pos += 1
    elif command[i] == 'L':
        pos -= 1
    roadpattern[i][pos] = '#'
    line = ''.join(c for c in roadpattern[i])
    print(line)
