import sys
import math

tributes = int(input())
player = []
for i in range(tributes):
    player.append(input())
player.sort()

killed = {}
killedBy = {}
turns = int(input())
for i in range(turns):
    info = input().split()
    killer = info[0]
    if killer not in killed:
        killed[killer] = []
    for victim in info[2:]:
        if victim[-1]==',':
            victim = victim[:-1]
        killed[killer].append(victim)
        killedBy[victim] = killer

first = True
for name in player:
    if not first:
        print("")
    print("Name: {}".format(name))
    if name in killed:
        killed[name].sort()
        temp = ""
        for i in range(len(killed[name])-1):
            temp += killed[name][i] + ", "
        temp += killed[name][-1]
    else:
        temp = "None"
    print("Killed: {}".format(temp))
    if name in killedBy:
        temp = killedBy[name]
    else:
        temp = "Winner"
    print("Killer: {}".format(temp))
    first = False
