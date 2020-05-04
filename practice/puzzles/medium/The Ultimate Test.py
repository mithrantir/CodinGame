def number_to_base(n, b, l):
    if n == 0:
        return [0 for i in range(l)]
    digits = []
    while len(digits) < l:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def combine(n, pattern):
    s = ""
    for i in range(len(pattern)):
        s += n[i] + pattern[i]
    s += n[-1]
    return s


n, k = input(), int(input())

action = ["", "+", "-"]
for ii in range(3 ** (len(n) - 1)):
    pattern = combine(n, [action[i] for i in number_to_base(ii, 3, len(n) - 1)])
    if eval(pattern) == k:
        print(pattern)
