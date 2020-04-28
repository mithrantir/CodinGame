import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rotor = []


def encode(s, num):
    s_shift = ""
    for i in range(len(s)):
        s_shift += chr((ord(s[i]) + num + i - ord('A')) % 26 + ord('A'))

    encoded = [c for c in s_shift]
    for r in range(3):
        for i in range(len(encoded)):
            encoded[i] = rotor[r][ord(encoded[i]) - ord('A')]

    return "".join(c for c in encoded)


def decode(s, num):
    plain = [c for c in s]
    for r in range(3):
        for i in range(len(plain)):
            plain[i] = chr(rotor[2 - r].index(plain[i]) + ord('A'))

    for i in range(len(plain)):
        plain[i] = chr((ord(plain[i]) - num - i - ord('A')) % 26 + ord('A'))

    return "".join(c for c in plain)


operation = input()
pseudo_random_number = int(input())
for i in range(3):
    rotor.append(input())
message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
if operation == "ENCODE":
    print(encode(message, pseudo_random_number))
else:
    print(decode(message, pseudo_random_number))
