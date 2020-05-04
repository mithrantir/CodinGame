position = {"TOP": 1, "LEFT": 0, "RIGHT": 2}
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
# coding room_types with the choices of "entry direction:exit direction"
room_types = {0: {}, 1: {0: 3, 1: 3, 2: 3}, 2: {0: 2, 2: 0}, 3: {1: 3},
              4: {1: 0, 2: 3}, 5: {1: 2, 0: 3}, 6: {0: 2, 2: 0}, 7: {1: 3, 2: 3},
              8: {0: 3, 2: 3}, 9: {0: 3, 1: 3}, 10: {1: 0}, 11: {1: 2}, 12: {2: 3}, 13: {0: 3}}

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
well_map = []
for i in range(h):
    # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    well_map.append([int(c) for c in input().split()])

ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    yi, xi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    d_vector = room_types[well_map[xi][yi]][position[pos]]
    nx, ny = xi + direction[d_vector][0], yi + direction[d_vector][1]

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print("{} {}".format(ny, nx))
