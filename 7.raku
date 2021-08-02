my @primes = (0..^∞).grep(&is-prime);

say @primes[10_000];
