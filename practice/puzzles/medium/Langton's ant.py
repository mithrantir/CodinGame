heading = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direction = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
color = {'#': 1, '.': 3}
color_inv = {1: '#', 3: '.'}

w, h = [int(i) for i in input().split()]
y, x = [int(i) for i in input().split()]
d = direction[input()]
t = int(input())
board = []
for i in range(h):
    board.append([color[c] for c in input()])

for i in range(t):
    d = (d + board[x][y]) % 4
    board[x][y] = 4 - board[x][y]
    x , y = x + heading[d][0], y + heading[d][1]

for i in range(h):
    line = ""
    for c in board[i]:
        line += color_inv[c]
    print(line)
