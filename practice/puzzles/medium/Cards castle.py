stability_msg = {True: "STABLE", False: "UNSTABLE"}

h = int(input())
castle, stable = [], True
for i in range(h):
    castle.append([c for c in input()])

for i in range(h):
    for j in range(2*h):
        if castle[i][j] == '/':
            if j == 2 * h - 1 or castle[i][j+1] != '\\' or (i < h - 1 and (castle[i+1][j] != '\\' or castle[i+1][j-1] != '/')):
                stable = False
                break
        elif castle[i][j] == '\\':
            if j == 0 or castle[i][j-1] != '/' or (i < h - 1 and (castle[i+1][j] != '/' or castle[i+1][j+1] != '\\')):
                stable = False
                break
    if not stable:
        break

print(stability_msg[stable])
