import math
import itertools

def sieve(n):
    A = [True] * n

    for i in range(2, math.floor(math.sqrt(n) + 1), 1):
        if A[i]:
            for j in range(i ** 2, n, i):
                A[j] = False

    primes = []

    for i, is_prime in enumerate(A):
        if is_prime:
            primes.append(i)

    return primes[2:]

primes = list(filter(lambda n: n >= 1_000, sieve(10_000)))

for a, b, c in itertools.permutations(primes, 3):
    if b - a + b == c:
        s_a = sorted(str(a))

        if s_a == sorted(str(b)):            
            if sorted(str(c)) == s_a:
                print(a, b, c)
