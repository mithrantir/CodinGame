
def gcd(a, b):
    if b == 0: return a
    else:
        return gcd(b, a%b)

n = int(input())
for i in range(n):
    x_s, y_s = input().split('/')
    x, y = int(x_s), int(y_s)
    if y==0:
        print("DIVISION BY ZERO")
    elif x==0:
        print(0)
    else:
        sign = x*y// abs(x*y)
        x , y = abs(x), abs(y)
        int_part, frac_part = x // y, x % y
        num , den = frac_part // gcd(frac_part, y), y // gcd(frac_part, y)
        if int_part == 0:
            ans = str(sign * num) + "/" + str(den)
        else:
            ans = str(sign*int_part)
            if frac_part != 0:
                ans += " " + str(num) + "/" + str(den)
        print(ans)
