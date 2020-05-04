

def bfs_from_to(st, fn):
    distance, bfs_list, arrived = {st: 0}, [st], False
    while len(bfs_list) > 0:
        node = bfs_list.pop(0)
        if node in move_from:
            for n in move_from[node]:
                if n not in distance:
                    distance[n] = distance[node] + 1
                    bfs_list.append(n)
                    if n == fn:
                        arrived = True
                        break
        if arrived:
            break
    return distance[fn]


f = open("000.txt", "r").read().split("\n")
ys, xs = [int(i) for i in f[0].split()]
yr, xr = [int(i) for i in f[1].split()]
w, h = [int(i) for i in f[2].split()]

# xs, ys = [int(i) for i in input().split()]
# xr, yr = [int(i) for i in input().split()]
# w, h = [int(i) for i in input().split()]
move_from = {}
for i in range(h):
    l = [str(bin(int(c, 16)))[2:] for c in f[3+i]]
    # l = [str(bin(int(c, 16)))[2:] for c in input()]

    l = [list(reversed([c for c in item])) for item in l]
    l = [[i for i, x in enumerate(item) if x == '1'] for item in l]
    for j in range(w):
        move_from[(i, j)] = []
        if 0 not in l[j]:
            move_from[(i, j)].append((i + 1, j))
        if 1 not in l[j]:
            move_from[(i, j)].append((i, j - 1))
        if 2 not in l[j]:
            move_from[(i, j)].append((i - 1, j))
        if 3 not in l[j]:
            move_from[(i, j)].append((i, j + 1))

print("{} {}".format(bfs_from_to((xs, ys), (xr, yr)), bfs_from_to((xr, yr), (xs, ys))))
