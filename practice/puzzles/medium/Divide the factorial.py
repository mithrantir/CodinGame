prime = [2,3]

def prime_list(n):
    global prime
    k = 5
    while k**2 <= n:
        ind, is_prime = 0, True
        while prime[ind]**2 <= k:
            if k % prime[ind] == 0:
                is_prime = False
                break
            ind += 1
        if is_prime:
            prime.append(k)
        k += 2
    return


def prime_pow_in_facorial(p, b):
    ans, temp = 0, b
    while temp > 1:
        ans += temp // p
        temp = temp // p
    return ans


a, b = [int(i) for i in input().split()]
prime_list(a)

ind, minpow = 0, b
while a > 1:
    while a % prime[ind] != 0:
        ind += 1
        if ind == len(prime):
            break
    if ind < len(prime):
        pw = 0
        while a % prime[ind] == 0:
            a, pw = a // prime[ind], pw + 1
        hold = prime_pow_in_facorial(prime[ind], b) // pw
    else:
        hold = prime_pow_in_facorial(a, b)
        a = 1
    minpow = min(minpow, hold)

print(minpow)
