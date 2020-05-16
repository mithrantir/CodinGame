
def to_decimal(num, b):
    res = 0
    for n in num:
        res = res * b + n
    return res


def is_polydivisible(n):
    n_s = str(n)
    for i in range(1, len(n_s) + 1):
        if int(n_s[:i]) % i != 0:
            return False
    return True


number = [int(c) for c in input().split()]
nb = max(number) + 1
for b in range(nb, 37):
    if is_polydivisible(to_decimal(number, b)):
        print(b)
