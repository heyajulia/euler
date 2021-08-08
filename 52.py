import itertools
import sys


def have_same_digits(a, b):
    s_a = str(a)
    s_b = str(b)

    return len(s_a) == len(s_b) and sorted(s_a) == sorted(s_b)


for x in itertools.count(start=2):
    if have_same_digits(x, 2 * x):
        if have_same_digits(x, 3 * x):
            if have_same_digits(x, 4 * x):
                if have_same_digits(x, 5 * x):
                    if have_same_digits(x, 6 * x):
                        print(x)

                        sys.exit(0)
