comes_from = {0: [5, 7], 1: [6, 8], 2: [3, 7], 3: [2, 8], 5: [0, 6], 6: [1, 5], 7: [0, 2], 8: [1, 3]}

start = (1, 2, 3, 4, 5, 6, 7, 8, 0)
distances = {start: 0}

def precowculation():
    global distances
    bfs = [list(start)]
    while len(bfs) > 0:
        temp = bfs.pop(0)
        ind = temp.index(0)
        for i in comes_from[ind]:
            hold = temp.copy()
            hold[i], hold[ind] = temp[ind], temp[i]
            if tuple(hold) not in distances:
                distances[tuple(hold)] = distances[tuple(temp)] + 1
                bfs.append(hold)
    return

precowculation()
target = []
for i in range(3):
    line = input()
    for c in line:
        if c.isdigit():
            target.append(int(c))
        else:
            target.append(0)

target = tuple(target)
if target in distances:
    print(distances[target])
else:
    print("-1")
