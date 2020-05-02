import re


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


f = open("000.txt", "r").read().split("\n")
expression = f[0]
# expression = input()

category = re.findall("[+|-][a-zA-Z]+", expression)


types = f[1].split(',')
# types = input().split(',')

order = []
sorting_type = {}
for cat in category:
    ind = category.index(cat)
    sorting_type[cat[1:]] = [types[ind], ind+1]
    if cat[0] == '+':
        order.append(False)
    else:
        order.append(True)
print(category)
print(order)


def compare_data(list1, list2):
    for i in range(1, len(list1)):
        if list1[i] != list2[i]:
            if order[i-1]:
                if list1[i] > list2[i]:
                    return -1
                else:
                    return 1
            else:
                if list1[i] < list2[i]:
                    return -1
                else:
                    return 1
    return list1[0] - list2[0]


n = int(f[2])
# n = int(input())

data = []
for i in range(n):
    row = [item.split(':') for item in f[3+i].split(',')]
    # row = [item.split(':') for item in input().split(',')]

    hold = [0 for c in range(len(category)+1)]
    for x, y in row:
        if x == 'id':
            hold[0] = int(y)
        elif x in sorting_type:
            if sorting_type[x][0] == 'int':
                y = int(y)
            hold[sorting_type[x][1]] = y
    data.append(hold)

data_srt = sorted(data, key = cmp_to_key(compare_data))

for l in data_srt:
    print(l[0])

