
n = int(input())
point = []

xmin, ymin, xmax, ymax = 25, 25, -25, -25
for i in range(n):
    x, y = [int(j) for j in input().split()]
    point.append((x, y))
    xmin, ymin, xmax, ymax = min(xmin, x), min(ymin, y), max(xmax, x), max(ymax, y)

xmin, ymin, xmax, ymax = min(xmin-1, -1), min(ymin-1, -1), max(xmax+1, 1), max(ymax+1, 1)
width, height = xmax - xmin + 1, ymax - ymin + 1
orx, ory = -xmin, height - 1 + ymin

graph = []
for i in range(height):
    graph.append([])
    for j in range(width):
        graph[i].append('.')

for i in range(height):
    graph[i][orx] = '|'
for i in range(width):
    graph[ory][i] = '-'
graph[ory][orx] = '+'

for x, y in point:
    graph[ory - y][x - xmin] = '*'

for line in graph:
    print("".join(c for c in line))
