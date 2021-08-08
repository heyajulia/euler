import itertools

print(
    max(
        map(
            lambda n: sum(map(int, str(n))),
            (a ** b for a, b in itertools.product(range(1, 101), range(1, 101))),
        )
    )
)
