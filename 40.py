import itertools

d = ""

for n in itertools.count(1):
    if len(d) >= 1_000_000: break
    d += str(n)

a = 1

for i in (0, 9, 99, 999, 9_999, 99_999, 999_999):
    a *= int(d[i])

print(a)
