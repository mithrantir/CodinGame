def rotate_counter(b):
    b_rot = []
    for m in range(nb - 1, -1, -1):
        for i in range(nb):
            b_rot.append(b[i * nb + m])
    return b_rot


def rotate_clock(b):
    b_rot = []
    for m in range(nb):
        for i in range(nb - 1, -1, -1):
            b_rot.append(b[nb * i + m])
    return b_rot


ii, nb, grid = int(input()) - 1, int(input()), []
for i in range(nb):
    grid += [c for c in input()]

ind, rot_status, move, status, reduced = 0, 0, 0, {(0, 0): 0}, False
while move < ii:
    move += 1

    while grid[ind] == '#' or grid[ind] == '@':
        if grid[ind] == '#':
            grid = rotate_clock(grid)
            rot_status = (rot_status + 1) % 4
        elif grid[ind] == '@':
            grid = rotate_counter(grid)
            rot_status = (rot_status + 3) % 4

    step = ord(grid[ind]) - ord('a') + 1
    ind = (ind + step) % (nb * nb)
    if not reduced:
        if (ind, rot_status) not in status:
            status[(ind, rot_status)] = move
        else:
            cycle = move - status[(ind, rot_status)]
            move = ii - (ii - move) % cycle

print(grid[ind])
