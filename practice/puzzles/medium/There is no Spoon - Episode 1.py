# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grid = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(line)

for i in range(width):
    for j in range(height):
        if grid[j][i] == '0':
            ans = str(i) + " " + str(j) + " "

            found, v = False, -1
            for k in range(i + 1, width):
                if grid[j][k] == '0':
                    found, v = True, k
                    break
            if found:
                ans += str(v) + " " + str(j) + " "
            else:
                ans += "-1 -1 "

            found, v = False, -1
            for k in range(j + 1, height):
                if grid[k][i] == '0':
                    found, v = True, k
                    break

            if found:
                ans += str(i) + " " + str(v)
            else:
                ans += "-1 -1"

            print(ans)
