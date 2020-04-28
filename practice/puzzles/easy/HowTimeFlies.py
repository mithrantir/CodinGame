import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

daysOf = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeap(n):
    if n % 4 != 0: return False
    if n % 400 == 0: return True
    if n % 100 == 0: return False
    return True


def daysFromStart(d, m, y):
    ndays = d
    for n in range(m):
        ndays += daysOf[n]
        if n == 2 and isLeap(y):
            ndays += 1

    return ndays

def daysToEnd(d, m, y):
    if isLeap(y) and m <= 2:
        ndays = 1
    else:
        ndays = 0
    ndays += daysOf[m]-d

    for n in range(m+1,13):
        ndays += daysOf[n]

    return ndays


f = open('00000.txt', 'r').read().split('\n')
begin = [int(c) for c in f[0].split('.')]
end = [int(c) for c in f[1].split('.')]

# begin = [int(c) for c in input().split('.')]
# end = [int(c) for c in input().split('.')]

ndays = 0
if begin[2] < end[2]:
    ndays = daysToEnd(begin[0], begin[1], begin[2]) + daysFromStart(end[0], end[1], end[2])
    for y in range(begin[2]+1, end[2]):
        if isLeap(y):
            ndays += 366
        else:
            ndays += 365
elif begin[1] < end[1]:
    for m in range(begin[1]+1, end[1]):
        ndays += daysOf[m]
        if m == 2 and isLeap(begin[2]):
            ndays += 1
    ndays += end[0] + daysOf[begin[1]] - begin[0]
    if begin[1] == 2 and isLeap(begin[2]):
        ndays += 1
else:
    ndays = end[0] - begin[0]

answer = ""
nyears = end[2] - begin[2]
if begin[1] > end[1]:
    nyears -= 1
elif begin[1] == end[1] and begin[0] > end[0]:
    nyears -= 1
if nyears > 0:
    answer += str(nyears) + " year"
    if nyears > 1:
        answer += "s"
    answer += ", "

if end[1] > begin[1]:
    nmonths = end[1]-begin[1]
    if begin[0] > end[0]:
        nmonths -= 1
elif end[1] == begin[1]:
    if begin[0] > end[0]:
        nmonths = 11
    else:
        nmonths=0
else:
    nmonths = 12 - begin[1] + end[1]
    if begin[0] > end[0]:
        nmonths -= 1
if nmonths > 0:
    answer += str(nmonths) + " month"
    if nmonths > 1:
        answer += "s"
    answer += ", "

answer += "total " + str(ndays) + " days"

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(answer)

