from functools import lru_cache
import itertools

@lru_cache(maxsize=None)
def d(n):
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum

def is_amicable_pair(a, b):
    return a != b and d(a) == b and d(b) == a

sum = 0

for a, b in itertools.product(range(1, 10_000), range(1, 10_000)):
    if is_amicable_pair(a, b):
        sum += a

print(sum)
