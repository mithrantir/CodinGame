def candidates(coord):
    i, j = coord[0], coord[1]
    candidate_list = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # check row and colums
    for a in range(9):
        candidate_list.discard(sudoku[i][a])
        candidate_list.discard(sudoku[a][j])

    # check box
    for a in range(3):
        for b in range(3):
            candidate_list.discard(sudoku[a + (i // 3) * 3][b + (j // 3) * 3])

    return candidate_list


def backtrack(n):
    global sudoku
    global solved

    if n == len(empty_positions):
        solved = True
        return

    cl = candidates(empty_positions[n])
    i, j = empty_positions[n][0], empty_positions[n][1]
    for k in cl:
        sudoku[i][j] = k
        backtrack(n + 1)
        if solved:
            return
    sudoku[i][j] = 0
    return


sudoku, solved = [], False
for i in range(9):
    sudoku.append([int(c) for c in input()])

empty_positions = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty_positions.append([i, j])

backtrack(0)
for i in range(9):
    print(''.join(str(n) for n in sudoku[i]))
