import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

answer = "."
for i in range(2,2*n):
    answer += " "
answer += "*\n"
for i in range(2,n+1):
    for j in range(1,2*n-i+1): answer += " "
    for j in range(1 , 2*i): answer += "*"
    answer += "\n"

for i in range(1,n+1):
    for j in range(1,n-i+1): answer += " "
    for j in range(1,2*i): answer += "*"
    for j in range(1,2*n+2-2*i): answer += " "
    for j in range(1,2*i):  answer += "*"
    if i < n: answer += "\n"

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
print(answer)


