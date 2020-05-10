# precowculation of all answers

sums = [[] for i in range(19)]
prods = [[] for i in range(82)]
for a in range(1, 10):
    for b in range(a, 10):
        sums[a + b].append([a, b])
        prods[a * b].append([a, b])

answer = {}
erased, round = True, 0
while erased:
    erased, round = False, round + 1

    for sm in range(len(sums)):
        if len(sums[sm]) == 1:
            erased = True
            a, b = sums[sm].pop()
            answer[(a, b)] = "BURT " + str(round)
            prods[a * b].remove([a, b])

    for pr in range(len(prods)):
        if len(prods[pr]) == 1:
            erased = True
            a, b = prods[pr].pop()
            answer[(a, b)] = "SARAH " + str(round)
            sums[a + b].remove([a, b])

x, y = int(input()), int(input())
delta = x**2 - 4 * y
a, b = (x - int(delta**(1/2))) // 2, (x + int(delta**(1/2))) // 2
if (a, b) not in answer:
    print("IMPOSSIBLE")
else:
    ans = "(" + str(a) + "," + str(b) + ") " + answer[(a,b)]
    print(ans)
