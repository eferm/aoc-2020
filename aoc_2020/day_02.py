import re
from collections import Counter
from _utils import *

inp = get_input(2020, 2)
print(inp[:78])
print(len(inp))

lines = inp.strip().split("\n")


def split(line):
    regex = re.compile(r"(\d+)\-(\d+) (\w): (\w+)")
    return regex.match(line).groups()


# part 1
valid = 0
for line in lines:
    min_, max_, char, pw = split(line)
    if int(min_) <= Counter(pw)[char] <= int(max_):
        valid += 1

print(valid)

# part 2
valid = 0
for line in lines:
    a, b, char, pw = split(line)
    if (pw[int(a) - 1] == char) != (pw[int(b) - 1] == char):
        valid += 1

print(valid)
