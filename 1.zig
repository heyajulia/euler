const std = @import("std");
const print = std.debug.print;

fn isMultipleOfThreeOrFive(n: usize) bool {
    if (n % 3 == 0) {
        return true;
    }

    if (n % 5 == 0) {
        return true;
    }

    return false;
}

pub fn main() void {
    var sum: usize = 0;
    var n: usize = 0;

    while (n < 1_000) : (n += 1) {
        if (isMultipleOfThreeOrFive(n)) {
            sum += n;
        }
    }

    print("{}\n", .{sum});
}
