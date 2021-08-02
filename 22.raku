my @names = sort "p022_names.txt".IO.split(",").map(*.subst('"', "", :g));
my %names = (@names Z 1..@names.elems).flat;

sub score-name($name) {
    my $name-index = %names{$name};

    return $name-index * [+] $name.comb.map(-> $letter { ord($letter) - ord('A') + 1 });
}

say [+] @names.map(&score-name);
