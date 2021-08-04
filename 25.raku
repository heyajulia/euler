my @F = 1, 1, * + * ... ∞;

say @F.first(*.chars == 1000, :k) + 1;
