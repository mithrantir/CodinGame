
w, h = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]

maze = []
for i in range(h):
    maze.append([c for c in input()])

maze[x][y] = '#'
exits, bfs = [], [[x, y]]
while len(bfs) > 0 :
    x, y = bfs.pop(0)
    if x + 1 < h and maze[x + 1][y] == '.':
        if x + 1 == h - 1:
            exits.append([x + 1, y])
        maze[x + 1][y] = '#'
        bfs.append([x + 1, y])
    if y + 1 < w and maze[x][y + 1] == '.':
        if y + 1 == w - 1:
            exits.append([x, y + 1])
        maze[x][y + 1] = '#'
        bfs.append([x, y + 1])
    if x > 0 and maze[x - 1][y] == '.':
        if x == 1:
            exits.append([x - 1, y])
        maze[x - 1][y] = '#'
        bfs.append([x - 1, y])
    if y > 0 and maze[x][y - 1] == '.':
        if y == 1:
            exits.append([x, y - 1])
        maze[x][y - 1] = '#'
        bfs.append([x, y - 1])

exits.sort(key = lambda x: (x[1],x[0]))
print(len(exits))
for x , y in exits:
    print("{} {}".format(y, x))
