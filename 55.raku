sub is-palindrome($n) { $n == $n.comb.reverse.join }

sub is-Lychrel-number($n is copy) {
    my $iterations = 0;

    while $iterations < 50 {
        $iterations++;

        $n += $n.comb.reverse.join;

        return False if is-palindrome $n;
    }

    return True;
}

(0..10_000).race.grep(&is-Lychrel-number).elems.say;
