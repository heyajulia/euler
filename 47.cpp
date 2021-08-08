#include <iostream>

static unsigned int count_distinct_prime_factors(unsigned int n)
{
    unsigned int distinct_prime_factors = 0;
    unsigned int factor = 2;
    bool counted = false;

    while (n > 1)
    {
        if (n % factor == 0)
        {
            if (!counted)
            {
                counted = true;
                distinct_prime_factors++;
            }

            n /= factor;
        }
        else
        {
            counted = false;
            factor++;
        }
    }

    return distinct_prime_factors;
}

int main()
{
    for (unsigned int i = 1;; i++)
    {
        if (count_distinct_prime_factors(i) == 4 && count_distinct_prime_factors(i + 1) == 4 &&
            count_distinct_prime_factors(i + 2) == 4 && count_distinct_prime_factors(i + 3) == 4)
        {
            std::cout << i << std::endl;
            return 0;
        }
    }
}
