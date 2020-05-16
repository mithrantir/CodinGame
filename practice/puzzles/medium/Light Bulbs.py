
def grey_to_decimal(s):
    num, ind = 0, 0
    while ind < len(s):
        num = 2 * num + s[ind]
        ind += 1
    return num


def grey_to_bin(s):
    num = grey_to_decimal(s)
    mask = num // 2
    while mask != 0:
        num = num ^ mask
        mask = mask // 2
    return num


s = [int(c) for c in input()]
t = [int(c) for c in input()]

print(abs(grey_to_bin(s) - grey_to_bin(t)))
