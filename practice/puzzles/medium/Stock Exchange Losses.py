
n = int(input())
maxf, best = 0, 0
for i in input().split():
    v = int(i)
    if v > maxf:
        maxf = v
    elif best > v-maxf:
        best = v-maxf
print(best)
