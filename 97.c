/**
 * This program depends on the GNU Multiple Precision Arithmetic Library, which
 * can be installed using `brew install gmp` on macOS.
 *
 * Then you can compile this program using a command like:
 *
 *     clang -I(brew --prefix)/include -L(brew --prefix)/lib -o 97 -lgmp 97.c
 */

#include <gmp.h>

int main()
{
    mpz_t result;

    mpz_init(result);

    mpz_ui_pow_ui(result, 2, 7830457); // result = 2⁷⁸³⁰⁴⁵⁷;
    mpz_mul_ui(result, result, 28433); // result *= 28433;
    mpz_add_ui(result, result, 1);     // result += 1;

    gmp_printf("%Zd\n", result);

    mpz_clear(result);
}
