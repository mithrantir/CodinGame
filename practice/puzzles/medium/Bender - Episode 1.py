

mode = {"inverter": False, "breaker": False}
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
acronym_of_dirs = ["S", "E", "N", "W"]
name_of_dirs = ["SOUTH", "EAST", "NORTH", "WEST"]
state_of_game = set()
path = []


def find_next_direction(x, y, d):
    priority = [d, 0, 1, 2, 3]
    for i in priority:
        tempx, tempy = x + directions[i][0], y + directions[i][1]
        if 0 <= tempx < l and 0 <= tempy < c:
            if arena[tempx][tempy] != '#' and (mode["breaker"] or arena[tempx][tempy] != 'X'):
                return i
    return None


def resolve_next_move(x, y, d):
    global arena, nOfX
    nx, ny, nd = x + directions[d][0], y + directions[d][1], d
    if arena[nx][ny] == 'I':
        mode["inverter"] = not mode["inverter"]
        name_of_dirs.reverse()
        acronym_of_dirs.reverse()
        directions.reverse()
        nd = 3 - nd
    elif arena[nx][ny] == 'B':
        mode["breaker"] = not mode["breaker"]
    elif arena[nx][ny] in acronym_of_dirs:
        nd = acronym_of_dirs.index(arena[nx][ny])
    elif arena[nx][ny] == 'X':
        arena[nx][ny], nOfX = ' ', nOfX - 1
    elif arena[nx][ny] == 'T':
        nx, ny = teleport[(teleport.index([nx, ny])+1) % 2]

    nd = find_next_direction(nx, ny, nd)
    return nx, ny, nd


f = open("000.txt", 'r').read().split('\n')    # file input
l, c = map(int, f[0].split())                  # file input

# l, c = [int(i) for i in input().split()]     # console input
arena = []
for i in range(l):
    row = f[1+i]                # file input
    # row = input()             # console input
    arena.append([c for c in row])

# mark special positions (starting, suicide booth, teleports)
# and the number of X's to recognise state repetitions
teleport = []
stx, sty, fnx, fny, nOfX = -1, -1, -1, -1, 0
for x in range(l):
    for y in range(c):
        if arena[x][y] == '@':
            prx, pry, arena[x][y] = x, y, ' '
        elif arena[x][y] == '$':
            fnx, fny = x, y
        elif arena[x][y] == 'T':
            teleport.append([x, y])
        elif arena[x][y] == 'X':
            nOfX += 1

d = find_next_direction(prx, pry, 0)
state_of_game.add((prx, pry, d, nOfX, mode["inverter"], mode["breaker"]))
while True:
    path.append(name_of_dirs[d])
    prx, pry, d = resolve_next_move(prx, pry, d)
    if prx == fnx and pry == fny:
        for dr in path:
            print(dr)
        break

    state = (prx, pry, d, nOfX, mode["inverter"], mode["breaker"])
    if state in state_of_game:
        print("LOOP")
        break
    else:
        state_of_game.add(state)
