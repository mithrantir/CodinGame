def update_bomb(x, y, d):
    global bomb_pos
    if d == "U":
        bomb_pos[0][1], bomb_pos[1][1], bomb_pos[1][0] = y, y, x
    elif d == "UR":
        bomb_pos[1][0], bomb_pos[0][1] = x, y
    elif d == "R":
        bomb_pos[0][0], bomb_pos[1][0], bomb_pos[0][1] = x, x, y
    elif d == "DR":
        bomb_pos[0][0], bomb_pos[0][1] = x, y
    elif d == "D":
        bomb_pos[0][1], bomb_pos[1][1], bomb_pos[0][0] = y, y, x
    elif d == "DL":
        bomb_pos[0][0], bomb_pos[1][1] = x, y
    elif d == "L":
        bomb_pos[0][0], bomb_pos[1][0], bomb_pos[1][1] = x, x, y
    elif d == "UL":
        bomb_pos[1][0], bomb_pos[1][1] = x, y
    return


# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
y0, x0 = [int(i) for i in input().split()]

# bomb_pos = [[xmin, ymin],[xmax,ymax]]
bomb_pos = [[0, 0], [h, w]]
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    update_bomb(x0, y0, bomb_dir)

    # the location of the next window Batman should jump to.
    x0 = (bomb_pos[0][0] + bomb_pos[1][0]) // 2
    y0 = (bomb_pos[0][1] + bomb_pos[1][1]) // 2
    print("{} {}".format(y0, x0))
