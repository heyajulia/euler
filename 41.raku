# I solved this problem interactively using the REPL.
<1 2 3 4 5 6 7>.permutations.map(*.join).grep(&is-prime).max.say;
