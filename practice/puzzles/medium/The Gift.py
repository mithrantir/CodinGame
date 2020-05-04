import sys

n = int(input())
c = int(input())

budget, total = [], 0
for i in range(n):
    budget.append(int(input()))
    total += budget[i]

if total < c:
    print("IMPOSSIBLE")
else:
    budget.sort(reverse=True)
    print(budget, file=sys.stderr)
    contribution = [0 for i in range(n)]
    while c > 0:
        print(budget, file=sys.stderr)
        mean = max(1, c // n)
        # print("{} {}".format(c,mean), file=sys.stderr)
        for i in range(n):
            if 0 < budget[i] <= mean:
                contribution[i] += budget[i]
                c -= budget[i]
                if c == 0:
                    break
                budget[i] = 0
                n -= 1
            elif budget[i] > mean:
                contribution[i] += mean
                c -= mean
                if c == 0:
                    break
                budget[i] -= mean
    contribution.sort()
    for c in contribution:
        print(c)

