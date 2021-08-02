sub reverse-number($n) {
    my $num = $n;
    my $reversed-number = 0;

    while ($num > 0) {
        $reversed-number *= 10;
        $reversed-number += $num % 10;
        $num = $num div 10; # Integer divison.
    }

    return $reversed-number;
}

multi sub is-palindrome(Int $n) { $n == reverse-number($n) }
multi sub is-palindrome(Str $n) { $n == $n.comb.reverse.join }

(0..1_000_000)
    .grep(&is-palindrome)
    .map(*.base: 2)
    .grep(&is-palindrome)
    .map(*.parse-base: 2)
    .sum
    .say;
