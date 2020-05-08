
n = int(input())
start = [i for i in range(1, n + 1)]

p, queneau, term_list = start.copy(), True, []
for i in range(n):
    pn = []
    while len(p) > 1:
        pn.append(p.pop())
        pn.append(p.pop(0))
    pn = pn + p
    term_list.append(pn.copy())
    p = pn

if term_list[-1] == start:
    for p in term_list:
        pr_form = ""
        for i in range(n - 1):
            pr_form += str(p[i]) + ","
        pr_form += str(p[n - 1])
        print(pr_form)
else:
    print("IMPOSSIBLE")
