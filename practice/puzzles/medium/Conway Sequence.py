
def next_term(s):
    sl, ns = [int(c) for c in s.split()], ""
    while len(sl) > 0:
        first, nf = sl.pop(0), 1
        while len(sl) > 0 and first == sl[0]:
            sl.pop(0)
            nf += 1
        ns += str(nf) + " " + str(first) + " "
    return ns.strip()


r = input()
for n in range(1, int(input())):
    r = next_term(r)
print(r)
