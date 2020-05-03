
n = int(input())
ycoord, xmin, xmax = [], 2**31, -2**31
for i in range(n):
    x, y = [int(j) for j in input().split()]
    ycoord.append(y)
    if x < xmin:
        xmin = x
    if x > xmax:
        xmax = x

ycoord.sort()
answer, ymead = xmax - xmin, ycoord[n//2]
for y in ycoord:
    answer += abs(y - ymead)

print(answer)
