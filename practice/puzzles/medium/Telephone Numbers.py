
def common_prefix_length(s1, s2):
    n, ans = min(len(s1), len(s2)), 0
    while ans < n and s1[ans] == s2[ans]:
        ans += 1
    return ans


n = int(input())
telephone = []
for i in range(n):
    telephone.append(input())

telephone.sort()
tel1 = telephone.pop(0)
number = len(tel1)
while len(telephone)>0:
    tel2 = telephone.pop(0)
    number += len(tel2) - common_prefix_length(tel1, tel2)
    tel1 = tel2

# The number of elements (referencing a number) stored in the structure.
print(number)
