from collections import Counter
from _utils import *

inp = get_input(2020, 6)
# print(inp[:86])

groups = inp.strip().split("\n\n")
# print(groups[:2])


# part 1
yes = 0
for group in groups:
    yes += len(set(group.replace("\n", "")))

print(yes)


# part 2
yes = 0
for group in groups:
    persons = group.split("\n")
    counts = Counter(group.replace("\n", ""))
    valid = [k for k, v in counts.items() if v == len(persons)]
    yes += len(valid)

print(yes)
