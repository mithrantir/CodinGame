n = int(input())
sandpile, big = [], []
for i in range(n):
    sandpile.append([int(c) for c in input()])
for i in range(n):
    row = [int(c) for c in input()]
    for j in range(n):
        sandpile[i][j] += row[j]
        if sandpile[i][j] > 3:
            big.append([i, j])

while len(big) > 0:
    x, y = big.pop()
    sandpile[x][y] -= 4
    if sandpile[x][y] > 3:
        big.append([x, y])

    if x > 0:
        sandpile[x - 1][y] += 1
        if sandpile[x - 1][y] == 4:
            big.append([x - 1, y])

    if y > 0:
        sandpile[x][y - 1] += 1
        if sandpile[x][y - 1] == 4:
            big.append([x, y - 1])

    if x < n - 1:
        sandpile[x + 1][y] += 1
        if sandpile[x + 1][y] == 4:
            big.append([x + 1, y])

    if y < n - 1:
        sandpile[x][y + 1] += 1
        if sandpile[x][y + 1] == 4:
            big.append([x, y + 1])

for i in range(n):
    print("".join(str(c) for c in sandpile[i]))
