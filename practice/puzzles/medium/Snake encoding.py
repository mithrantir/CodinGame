
n = int(input())
x = int(input()) % (n*n)
text = []
for i in range(n):
    text.append([c for c in input()])

text_tr, text_line = [[text[i][j] for i in range(n)] for j in range(n)], []
for i in range(n):
    if i % 2 == 0:
        text_line += reversed(text_tr[i])
    else:
        text_line += text_tr[i]

enc_text_line, enc_text_tr = [text_line[(i - x) % (n * n)] for i in range(n*n)], []
for i in range(n):
    if i % 2 == 0:
        enc_text_tr.append(list(reversed(enc_text_line[i * n: (i + 1) * n])))
    else:
        enc_text_tr.append(enc_text_line[i * n: (i + 1) * n])

enc_text = [[enc_text_tr[i][j] for i in range(n)] for j in range(n)]
for i in range(n):
    print("".join(c for c in enc_text[i]))
