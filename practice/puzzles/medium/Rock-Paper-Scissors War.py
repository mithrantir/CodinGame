looses_by = {'P': ['C', 'L'], 'R': ['P', 'S'], 'C': ['S', 'R'], 'L': ['R', 'C'], 'S': ['L', 'P']}

w, h, n = [int(i) for i in input().split()]
area = []
for i in range(h):
    area.append([c for c in input()])

while n > 0:
    temp = []

    for i in range(h):
        temp.append([])
        for j in range(w):

            enemies = set()
            if i > 0 and area[i - 1][j] in looses_by[area[i][j]]:
                enemies.add(area[i - 1][j])
            if i < h - 1 and area[i + 1][j] in looses_by[area[i][j]]:
                enemies.add(area[i + 1][j])
            if j > 0 and area[i][j - 1] in looses_by[area[i][j]]:
                enemies.add(area[i][j - 1])
            if j < w - 1 and area[i][j + 1] in looses_by[area[i][j]]:
                enemies.add(area[i][j + 1])

            if len(enemies) == 0:
                temp[i].append(area[i][j])
            elif len(enemies) == 1:
                temp[i].append(enemies.pop())
            else:
                a, b = enemies.pop(), enemies.pop()
                if a in looses_by[b]:
                    temp[i].append(a)
                else:
                    temp[i].append(b)

    for i in range(h):
        for j in range(w):
            area[i][j] = temp[i][j]
    n = n - 1

for i in range(h):
    print(''.join(c for c in area[i]))
