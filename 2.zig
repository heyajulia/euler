const std = @import("std");
const print = std.debug.print;

const Allocator = std.mem.Allocator;
const ArenaAllocator = std.heap.ArenaAllocator;
const ArrayList = std.ArrayList;
const page_allocator = std.heap.page_allocator;

fn f(n: usize) usize {
    if (n <= 1) {
        return n;
    }

    return f(n - 2) + f(n - 1);
}

fn fibonacciNumbers(allocator: *Allocator) ArrayList(usize) {
    var list = ArrayList(usize).init(allocator);
    list.append(1) catch unreachable;

    var n: usize = 0;

    while (true) {
        var result = f(n);
        n += 1;

        if (result > 4_000_000) {
            break;
        }

        list.append(result) catch unreachable;
    }

    return list;
}

pub fn main() void {
    var arena = ArenaAllocator.init(page_allocator);
    defer arena.deinit();

    var sum: usize = 0;
    var numbers = fibonacciNumbers(&arena.allocator);

    for (numbers.items) |n| {
        if (n % 2 == 0) {
            sum += n;
        }
    }

    print("{}\n", .{sum});
}
