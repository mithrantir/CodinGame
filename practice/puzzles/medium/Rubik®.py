# A005897		a(n) = 6*n^2 + 2 for n > 0, a(0)=1.

n = int(input())

if n == 1:
    print(1)
else:
    print(6*(n-1)**2 + 2)
