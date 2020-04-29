import sys
import math

op_bowls = input().split()
my_bowls = input().split()
num = int(input())

ind, mine, n = num, True, int(my_bowls[num])
my_bowls[ind] = '0'

while n > 0:
    ind += 1
    if mine and ind == 7:
        mine = False
        ind = 0
    elif not mine and ind == 6:
        mine = True
        ind = 0
    if mine:
        my_bowls[ind] = str(int(my_bowls[ind])+1)
    else:
        op_bowls[ind] = str(int(op_bowls[ind])+1)
    n -= 1

if mine and ind == 6:
    replay = True
else:
    replay = False

ans = "".join(op_bowls[i] + " " for i in range(6))
ans += "[" + op_bowls[6] + "]\n"
ans += "".join(my_bowls[i] + " " for i in range(6))
ans += "[" + my_bowls[6] + "]"
print(ans)
if replay: print("REPLAY")