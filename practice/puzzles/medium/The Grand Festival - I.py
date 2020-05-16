
n = int(input())
r = int(input())
sol = [[0 for i in range(r+1)]]
for i in range(n):
    prize = int(input())
    sol.append([max(sol[-1])] + [prize + sol[-1][j] for j in range(r)])

print(max(sol[-1]))
