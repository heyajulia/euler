import math

max_value = 0.0

with open("p099_base_exp.txt") as f:
    for (line_number, line) in enumerate(f, start=1):
        (base, exponent) = line.split(",")

        if (value := math.log(int(base)) * int(exponent)) > max_value:
            print(line_number)

            max_value = value
