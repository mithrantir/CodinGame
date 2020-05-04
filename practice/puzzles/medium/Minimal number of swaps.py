
n = int(input())

zero_pos, n_of_ones = [], 0
line = input().split()
for i in range(n):
    x = int(line[i])
    if x == 1:
        n_of_ones += 1
    else:
        zero_pos.append(i)

ans, i = 0, 0
if len(zero_pos) > 0:
    while zero_pos[i] < n_of_ones:
        ans, i = ans + 1, i + 1

print(ans)
