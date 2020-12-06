import re
from collections import Counter
from _utils import *

inp = get_input(2020, 2)
lines = inp.strip().split("\n")


def split(line):
    regex = re.compile(r"(\d+)\-(\d+) (\w): (\w+)")
    return regex.match(line).groups()


# part 1


def validate1(line):
    min_, max_, char, pw = split(line)
    return int(min_) <= Counter(pw)[char] <= int(max_)


valid = map(validate1, lines)
print(sum(valid))


# part 2


def validate2(line):
    a, b, char, pw = split(line)
    # xor password chars at a and b
    return (pw[int(a) - 1] == char) != (pw[int(b) - 1] == char)


valid = map(validate2, lines)
print(sum(valid))
