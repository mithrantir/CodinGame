import sys
import math

succesion = []
childOf = {}
died = {}
birthOf = {}
religionOf = {}
genderOf = {}


def priority(person1, person2):
    if genderOf[person1] == 'M' and genderOf[person2] == 'F':
        return True
    elif genderOf[person1] == 'F' and genderOf[person2] == 'M':
        return False
    elif birthOf[person1] < birthOf[person2]:
        return True
    else:
        return False


def dfs(parent):
    global succesion
    if (not died[parent]) and religionOf[parent] != "Catholic":
        succesion.append(parent)
    if parent in childOf:
        for child in childOf[parent]:
            dfs(child)


n = int(input())
for i in range(n):
    name, parent, birth, death, religion, gender = input().split()
    birth = int(birth)
    if parent in childOf:
        childOf[parent].append(name)
    else:
        childOf[parent] = [name]
    if death == '-':
        died[name] = False
    else:
        died[name] = True
    birthOf[name] = birth
    religionOf[name] = religion
    genderOf[name] = gender

for p in childOf:  # bubblesort of the succcesors
    nc = len(childOf[p])
    for i in range(nc):
        for j in range(nc - 1):
            if not priority(childOf[p][j], childOf[p][j + 1]):
                childOf[p][j], childOf[p][j + 1] = childOf[p][j + 1], childOf[p][j]

dfs(childOf['-'][0])

for person in succesion:
    print(person)
