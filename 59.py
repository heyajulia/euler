import itertools
import string

def score_string(s):
    score = 0.0
    frequencies = {
        ord("e"): 0.13,
        ord("t"): 0.091,
        ord("a"): 0.082,
        ord("o"): 0.075,
        ord("i"): 0.07,
        ord("n"): 0.067,
        ord("s"): 0.063,
        ord("h"): 0.061,
        ord("r"): 0.06,
        ord("d"): 0.043,
        ord("l"): 0.04,
        ord("c"): 0.028,
        ord("u"): 0.028,
        ord("m"): 0.024,
        ord("w"): 0.024,
        ord("f"): 0.022,
        ord("g"): 0.02,
        ord("y"): 0.02,
        ord("p"): 0.019,
        ord("b"): 0.015,
        ord("v"): 0.0098,
        ord("k"): 0.0077,
        ord("j"): 0.0015,
        ord("x"): 0.0015,
        ord("q"): 0.00095,
        ord("z"): 0.00074,
    }

    for ch in s:
        score += frequencies.get(ch, -0.1)

    return score


message = []

with open("p059_cipher.txt") as f:
    for value in f.read().split(","):
        message.append(int(value))

max_score = 0.0

for key in itertools.permutations(list(string.ascii_lowercase), 3):
    key_repeating = map(ord, (key * len(message))[:len(message)])
    decoded_message = [message[i] ^ k for i, k in enumerate(key_repeating)]
    score = score_string(decoded_message)

    if score > max_score:
        max_score = score
        print(sum(decoded_message))
