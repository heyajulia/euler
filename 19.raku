sub is-sunday(Date $date --> Bool) { $date.day-of-week == 7 }

sub is-first-of-month(Date $date --> Bool) { $date.day-of-month == 1 }

my Date() $start = "1901-01-01";
my Date() $end   = "2000-12-31";

($start..$end).grep(&is-sunday & &is-first-of-month).elems.say;
