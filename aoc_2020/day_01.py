import math
from itertools import combinations

from _utils import *

inp = get_input(2020, 1)
nums = lmap(int, inp.strip().split())


def sum2020(n):
    for t in combinations(nums, n):
        if sum(t) == 2020:
            yield t


# part 1
print(math.prod(next(sum2020(2))))

# part 2
print(math.prod(next(sum2020(3))))
