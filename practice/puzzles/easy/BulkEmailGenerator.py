import sys
import math
import re


def choice(choices):
    global nchoice
    choices_list = choices.group()[1:-1].split('|')
    choose = choices_list[nchoice % len(choices_list)]
    nchoice += 1
    return choose


n = int(input())
temp = []
for i in range(n):
    temp.append(input())
email_pattern = "\n".join(s for s in temp)

nchoice = 0
email = re.sub('\([^)]*\)', choice, email_pattern)
print(email)
