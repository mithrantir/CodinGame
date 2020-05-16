
def number_at(s):
    ind = 0
    while s[ind].isdigit():
        ind += 1
        if ind == len(s):
            break
    return int(s[:ind]), ind


def evaluate(expr):
    global result
    for i in range(1, len(expr)):
        num, ind = number_at(expr[i])
        hold = []
        for ex in result:
            for j in range(1, num + 1):
                hold.append(ex + str(j) + expr[i][ind:])
        result = hold


expr = input().split('d')
result = [expr[0]]
evaluate(expr)
cases, freq = [], {}
for ex in result:
    cases.append(int(eval(ex)))

cases.sort()
for n in cases:
    if n not in freq:
        freq[n] = cases.count(n)

nc = len(cases)
for n in freq:
    print("{} {:0.2f}".format(n, 100*freq[n]/nc))
