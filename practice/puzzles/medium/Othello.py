board = []
for i in range(8):
    board.append([c for c in input()])
colour, move = input().split()
py, px = ord(move[0]) - ord('a'), int(move[1]) - 1

if board[px][py] != '-':
    print("NOPE")
else:
    board[px][py] = colour
    if colour == 'B':
        cap = 'W'
    else:
        cap = 'B'
    legal = False

    if px > 0 and board[px - 1][py] == cap:
        i = 1
        while i <= px and board[px - i][py] == cap:
            i += 1
        if i <= px and board[px - i][py] == colour:
            legal = True
            for j in range(i):
                board[px - j][py] = colour

    if px > 0 and py < 7 and board[px - 1][py + 1] == cap:
        i = 1
        while i <= px and py + i < 8 and board[px - i][py + i] == cap:
            i += 1
        if i <= px and py + i < 8 and board[px - i][py + i] == colour:
            legal = True
            for j in range(i):
                board[px - j][py + j] = colour

    if py < 7 and board[px][py + 1] == cap:
        i = 1
        while py + i < 8 and board[px][py + i] == cap:
            i += 1
        if py + i < 8 and board[px][py + i] == colour:
            legal = True
            for j in range(i):
                board[px][py + j] = colour

    if px < 7 and py < 7 and board[px + 1][py + 1] == cap:
        i = 1
        while px + i < 8 and py + i < 8 and board[px + i][py + i] == cap:
            i += 1
        if px + i < 8 and py + i < 8 and board[px + i][py + i] == colour:
            legal = True
            for j in range(i):
                board[px + j][py + j] = colour

    if px < 7 and board[px + 1][py] == cap:
        i = 1
        while px + i < 8 and board[px + i][py] == cap:
            i += 1
        if px + i < 8 and board[px + i][py] == colour:
            legal = True
            for j in range(i):
                board[px + j][py] = colour

    if px < 7 and py > 0 and board[px + 1][py - 1] == cap:
        i = 1
        while px + i < 8 and py >= i and board[px + i][py - i] == cap:
            i += 1
        if px + i < 8 and py >= i and board[px + i][py - i] == colour:
            legal = True
            for j in range(i):
                board[px + j][py - j] = colour

    if py > 0 and board[px][py - 1] == cap:
        i = 1
        while py >= i and board[px][py - i] == cap:
            i += 1
        if py >= i and board[px][py - i] == colour:
            legal = True
            for j in range(i):
                board[px][py - j] = colour

    if px > 0 and py > 0 and board[px - 1][py - 1] == cap:
        i = 1
        while i <= px and i <= py and board[px - i][py - i] == cap:
            i += 1
        if i <= px and i <= py and board[px - i][py - i] == colour:
            legal = True
            for j in range(i):
                board[px - j][py - j] = colour

    if not legal:
        print("NULL")
    else:
        nw, nb = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'W':
                    nw += 1
                elif board[i][j] == 'B':
                    nb += 1
        print("{} {}".format(nw, nb))
