import re
from collections import Counter
from _utils import *

inp = get_input(2020, 2)
print(inp[:78])
print(len(inp))
pws = inp.strip().split("\n")

# part 1
valid = 0
for line in pws:
    regex = re.compile(r"(\d+)\-(\d+) (\w): (\w+)")
    min_, max_, char, pw = regex.match(line).groups()
    if int(min_) <= Counter(pw)[char] <= int(max_):
        valid += 1

print(valid)

# part 2
valid = 0
for line in pws:
    regex = re.compile(r"(\d+)\-(\d+) (\w): (\w+)")
    a, b, char, pw = regex.match(line).groups()
    if (pw[int(a) - 1] == char) != (pw[int(b) - 1] == char):
        valid += 1

print(valid)
