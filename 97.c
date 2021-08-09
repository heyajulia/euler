/**
 * This program depends on the GNU Multiple Precision Arithmetic Library, which
 * can be installed using `brew install gmp` on macOS.
 *
 * Then you can compile this program using a command like:
 *
 *     clang -I(brew --prefix)/include -L(brew --prefix)/lib -o 97 -lgmp 97.c
 */

#include <gmp.h>
#include <stdio.h>

int main()
{
    mpz_t result;

    mpz_init(result);

    mpz_ui_pow_ui(result, 2, 7830457);                                // result = 2 ** 7830457;
    mpz_mul_ui(result, result, 28433);                                // result *= 28433;
    mpz_add_ui(result, result, 1);                                    // result += 1;
    unsigned long last_ten_digits = mpz_fdiv_ui(result, 10000000000); // result % 10000000000;

    printf("%lu\n", last_ten_digits);

    mpz_clear(result);
}
