import math

n = int(input())
ng = int(math.floor(((1 + 8 * n) ** (1 / 2) - 1) / 2))
height, width = 4 * ng, 6 * ng - 1
picture = [[' ' for j in range(width)] for i in range(height)]


def putGlass(i, j):
    global picture
    for k in range(j, j + 5):
        picture[i][k] = '*'
    for k in range(j + 1, j + 4):
        picture[i - 3][k] = '*'
    picture[i - 1][j + 1], picture[i - 1][j + 3] = '*', '*'
    picture[i - 2][j + 1], picture[i - 2][j + 3] = '*', '*'
    return


for l in range(ng, 0, -1):
    for k in range(1, l + 1):
        putGlass(l * 4 - 1, 6 * (k - 1) + 3 * (ng - l))

for line in picture:
    print("".join(c for c in line))
