#include <stdbool.h>
#include <stdio.h>

static bool evenly_divisible(unsigned int n)
{
    for (unsigned int i = 1; i <= 20; i++)
    {
        if (n % i != 0)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    unsigned int n = 1;

    while (true)
    {
        if (evenly_divisible(n))
        {
            break;
        }

        n += 1;
    }

    printf("%d\n", n);

    return 0;
}
