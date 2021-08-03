(1..1_000).map({ $^a ** $^a }).sum.comb[* - 10 .. *].join.say;
