dec_to_mayan = ["" for i in range(20)]


def input_mayan():
    pw, num = int(input()) // h, 0
    for p in range(pw - 1, -1, -1):
        mayan = ""
        for k in range(h):
            mayan += input()
        num += dec_to_mayan.index(mayan) * 20 ** p
    return num


l, h = [int(i) for i in input().split()]
for i in range(h):
    numeral = input()
    for j in range(20):
        dec_to_mayan[j] += numeral[j * l: (j + 1) * l]

num1, num2 = input_mayan(), input_mayan()

operation = input()
if operation == '+':
    res = num1 + num2
elif operation == '-':
    res = num1 - num2
elif operation == '*':
    res = num1 * num2
else:
    res = num1 // num2

digs = []
while res > 0:
    digs.append(res % 20)
    res = res // 20
digs.reverse()
if len(digs) == 0:
    digs = [0]

for d in digs:
    for ln in range(h):
        print(dec_to_mayan[d][ln * l: (ln + 1) * l])
