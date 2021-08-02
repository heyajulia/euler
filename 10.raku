my @primes = (0..^2_000_000).grep(&is-prime);

say sum @primes;
