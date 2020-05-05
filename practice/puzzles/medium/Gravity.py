
width, height = [int(i) for i in input().split()]
ascii_map = []
for i in range(height):
    ascii_map.append([c for c in input()])

for j in range(width):
    num_of_dot = 0
    for i in range(height):
        if ascii_map[i][j] == '.':
            num_of_dot += 1
    for i in range(height):
        if i < num_of_dot:
            ascii_map[i][j] = '.'
        else:
            ascii_map[i][j] = '#'

for i in range(height):
    print("".join(c for c in ascii_map[i]))
