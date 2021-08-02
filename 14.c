#include <stdio.h>

static unsigned int collatz(unsigned int n)
{
    unsigned int terms = 1;

    while (n != 1)
    {
        terms++;

        if (n % 2 == 0)
        {
            n /= 2;
        }
        else
        {
            n = 3 * n + 1;
        }
    }

    return terms;
}

int main()
{
    unsigned int max_terms = 0;
    unsigned int n = 0;

    for (unsigned int i = 1; i <= 1000000; i++)
    {
        unsigned int terms = collatz(i);

        if (terms > max_terms)
        {
            max_terms = terms;
            n = i;
        }
    }

    printf("%d\n", n);
}
