# Find largest prime factor using trial divison.
sub largest-prime-factor ($n is rw) {
    my $largest-factor = 0;
    my $factor = 2;

    while $n > 1 {
        if $n %% $factor {
            $largest-factor = max $largest-factor, $factor;
            $n div= $factor;
        } else {
            $factor++;
        }
    }

    return $largest-factor;
}

my $n = 600851475143;

say largest-prime-factor $n;
