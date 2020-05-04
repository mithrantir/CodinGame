# A composite odd number n is a Carmichael number if and only if n is squarefree
# and p-1 divides n-1 for every prime p dividing n. (Korselt, 1899)


def calculate_primes(n):
    prime, k = [2, 3], 5
    while k < n:
        i, isprime = 1, True
        while prime[i] ** 2 <= k:
            if k % prime[i] == 0:
                isprime = False
                break
            i += 1
        if isprime:
            prime.append(k)
        k += 2
    return prime


def is_divisible(n, l):
    for p in l:
        if p ** 2 > n:
            return False
        elif n % p == 0:
            return True


prime = calculate_primes(1000)
prime_squared = [n ** 2 for n in prime]

n = int(input())

if not is_divisible(n, prime) or is_divisible(n, prime_squared):
    is_carmichael = False
else:
    m = n
    is_carmichael = True
    for p in prime:
        if p ** 2 > m:
            break
        if m % p == 0:
            m = m // p
            if (n - 1) % (p - 1) > 0:
                is_carmichael = False
    if m > 1 and (n - 1) % (m - 1) > 0:
        is_carmichael = False

if is_carmichael:
    print("YES")
else:
    print("NO")
