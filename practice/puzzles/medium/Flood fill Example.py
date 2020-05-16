
with open('000.txt') as f:
    read_data = f.read().split('\n')

w = int(read_data[0])
h = int(read_data[1])
# w = int(input())
# h = int(input())
alderaan = []
for i in range(h):
    # alderaan.append([c for c in input()])
    alderaan.append([c for c in read_data[2+i]])

tower = {}
for i in range(h):
    for j in range(w):
        if alderaan[i][j] != '.' and alderaan[i][j] != '#':
            tower[(i, j)] = [[i, j]]

expand = True
while expand:
    expand = False
    exp_points = {}
    for (tx, ty) in tower:
        tow_exp = []

        for i, j in tower[(tx, ty)]:
            if i > 0 and alderaan[i - 1][j] == '.':
                expand = True
                tow_exp.append([i-1, j])
                if (i - 1, j) in exp_points:
                    exp_points[(i - 1, j)] = '+'
                else:
                    exp_points[(i - 1, j)] = alderaan[tx][ty]
            if i < h - 1 and alderaan[i + 1][j] == '.':
                expand = True
                tow_exp.append([i + 1, j])
                if (i + 1, j) in exp_points:
                    exp_points[(i + 1, j)] = '+'
                else:
                    exp_points[(i + 1, j)] = alderaan[tx][ty]
            if j > 0 and alderaan[i][j - 1] == '.':
                expand = True
                tow_exp.append([i, j - 1])
                if (i, j - 1) in exp_points:
                    exp_points[(i, j - 1)] = '+'
                else:
                    exp_points[(i, j - 1)] = alderaan[tx][ty]
            if j < w - 1 and alderaan[i][j + 1] == '.':
                expand = True
                tow_exp.append([i, j + 1])
                if (i, j + 1) in exp_points:
                    exp_points[(i, j + 1)] = '+'
                else:
                    exp_points[(i, j + 1)] = alderaan[tx][ty]
        tower[(tx, ty)] = tow_exp

    if len(exp_points) == 0:
        expand = False
    else:
        for (i, j) in exp_points:
            alderaan[i][j] = exp_points[(i, j)]

for i in range(h):
    print("".join(c for c in alderaan[i]))
