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

sub is-palindrome(Int $n) { $n == reverse-number($n) }

cross(100..999, 100..999)
    .race
    .map(-> (\a, \b) { a * b })
    .grep(&is-palindrome)
    .max
    .say;
