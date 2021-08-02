const std = @import("std");
const print = std.debug.print;

fn sumOfSquares(n: usize) usize {
    var sum: usize = 0;
    var i: usize = 0;

    while (i <= n) : (i += 1) {
        sum += i * i;
    }

    return sum;
}

fn squareOfSum(n: usize) usize {
    var sum: usize = 0;
    var i: usize = 0;

    while (i <= n) : (i += 1) {
        sum += i;
    }

    return sum * sum;
}

pub fn main() void {
    const N: usize = 100;
    var difference = squareOfSum(N) - sumOfSquares(N);

    print("{}\n", .{difference});
}
