import sys
import math


def encode(s):
    ls, cipher, step = len(s), "", 1
    while len(cipher) < ls:
        cipher = cipher + s[:step]
        s = s[step:]
        step += 1
        cipher = s[:step] + cipher
        s = s[step:]
        step += 1
    return cipher


def decode(cipher):
    lc, plain, step, sm = len(cipher), "", 0, 0
    while sm + step <= lc:
        sm, step = sm + step, step + 1
    step -= 1

    if step % 2 == 1:
        plain = cipher[:lc - sm]
        cipher = cipher[lc - sm:]
    else:
        plain = cipher[sm:]
        cipher = cipher[:sm]

    while len(plain) < lc:
        if step % 2 == 1:
            plain = cipher[sm - step:] + plain
            cipher = cipher[:sm - step]
        else:
            plain = cipher[:step] + plain
            cipher = cipher[step:]
        sm, step = sm - step, step - 1
    return plain


n = int(input())
message = input()

while n < 0:
    message = encode(message)
    n += 1

while n > 0:
    message = decode(message)
    n -= 1

print(message)