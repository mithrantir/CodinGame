n1, n2 = [int(i) for i in input().split()]
s1, s2, t = input(), input(), int(input())

ans = ["" for c in range(n1 + n2)]
for i in range(n1):
    ans[min(n1 - 1 + n2 - i, n1 - 1 - i + max(t - i, 0))] = s1[i]

for i in range(n2):
    ans[max(i, n1 + i - max(t - i, 0))] = s2[i]

print("".join(c for c in ans))
