from functools import partial

from _utils import *

inp = get_input(2020, 6)
groups = inp.strip().split("\n\n")


def count(agg, group):
    return len(agg(*[set(p) for p in group.split()]))


# part 1
print(sum(map(partial(count, set.union), groups)))

# part 2
print(sum(map(partial(count, set.intersection), groups)))
