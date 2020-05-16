def path_of(num, den):
    if num < den:
        ans, n1, d1, n2, d2 = "L", 0, 1, 1, 1
    else:
        ans, n1, d1, n2, d2 = "R", 1, 1, 1, 0
    nn, dn = n1 + n2, d1 + d2
    while num * dn != den * nn:
        if num * dn < den * nn:
            ans, n2, d2 = ans + "L", nn, dn
        else:
            ans, n1, d1 = ans + "R", nn, dn
        nn, dn = n1 + n2, d1 + d2
    return ans


def rational_of(s):
    if s[0] == 'L':
        n1, d1, n2, d2 = 0, 1, 1, 1
    else:
        n1, d1, n2, d2 = 1, 1, 1, 0
    for c in s[1:]:
        if c == 'L':
            n2, d2 = n1 + n2, d1 + d2
        else:
            n1, d1 = n1 + n2, d1 + d2
    return str(n1 + n2) + '/' + str(d1 + d2)


n = int(input())
for i in range(n):
    line = input()
    if line[0].isdigit():
        n, d = [int(c) for c in line.split('/')]
        print(path_of(n, d))
    else:
        print(rational_of(line))
