import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

f = open('00000.txt', 'r')

# CONSOLE: rounds = int(input())
# CONSOLE: cash = int(input())
rounds = int(f.readline())
cash = int(f.readline())

for i in range(rounds):
    bet = int(math.ceil(cash / 4))
    play = f.readline().split()
    # CONSOLE: play = input()
    result = int(play[0])

    if play[1] == 'PLAIN':
        num = int(play[2])
        if result == num:
            cash += 35*bet
        else:
            cash -= bet
    elif play[1] == 'ODD':
        if result % 2 == 1:
            cash += bet
        else:
            cash -= bet
    else:
        if result % 2 == 0 and result > 0:
            cash += bet
        else:
            cash -= bet

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(cash)
