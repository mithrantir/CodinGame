
def value(i, j):
    val = 0
    if i < height - 1 and j < width - 1:
        val += colony[i+1][j+1]
    if i < height - 1:
        val += colony[i+1][j]
    if i < height - 1 and j > 0:
        val += colony[i+1][j-1]
    if j > 0:
        val += colony[i][j-1]
    if i > 0 and j > 0:
        val += colony[i-1][j-1]
    if i > 0:
        val += colony[i-1][j]
    if i > 0 and j < width - 1:
        val += colony[i-1][j+1]
    if j < width - 1:
        val += colony[i][j+1]
    return val


def next_generation(colony):
    offsprings = []
    for i in range(height):
        offsprings.append([])
        for j in range(width):
            if colony[i][j] == 1:
                if 2 <= value(i, j) <= 3:
                    offsprings[i].append(1)
                else:
                    offsprings[i].append(0)
            else:
                if value(i, j) == 3:
                    offsprings[i].append(1)
                else:
                    offsprings[i].append(0)
    return offsprings


width, height = [int(i) for i in input().split()]
colony = []
for i in range(height):
    colony.append([int(c) for c in input()])

for line in next_generation(colony):
    print("".join(str(c) for c in line))
