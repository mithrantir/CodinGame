def is_magic(square):
    sums, diag1, diag2, flatten = [], [], [], []
    for i in range(n):
        flatten += square[i]
        sums.append(sum(square[i]))
        sums.append(sum([square[j][i] for j in range(n)]))
        diag1.append(square[i][i])
        diag2.append(square[n - 1 - i][i])

    if max(flatten) != n * n or min(flatten) != 1 or len(set(flatten)) != n * n:
        return False

    sums.append(sum(diag1))
    sums.append(sum(diag2))
    return len(set(sums)) == 1


n = int(input())
square = []
for i in range(n):
    square.append([int(j) for j in input().split()])

msg = {True: "MAGIC", False: "MUGGLE"}
print(msg[is_magic(square)])
