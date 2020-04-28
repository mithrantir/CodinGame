import sys
import math

edges = {}


def bfs(v):
    distance, bfs_queue = {}, [v]
    distance[v] = 0
    maxd, maxv = 0, 0

    while len(bfs_queue) > 0:
        fv = bfs_queue.pop(0)
        for v in edges[fv]:
            if v not in distance:
                distance[v] = distance[fv] + 1
                if distance[v] > maxd:
                    maxd, maxv = distance[v], v
                bfs_queue.append(v)

    return maxv, maxd


n = int(input())
for i in range(n):
    a, b = [int(j) for j in input().split()]
    if a == b: continue
    if a in edges:
        edges[a].append(b)
    else:
        edges[a] = [b]
    if b in edges:
        edges[b].append(a)
    else:
        edges[b] = [a]

maxv, maxd = bfs(1)
maxv, maxd = bfs(maxv)
ans = (maxd + 1) // 2
print(ans)