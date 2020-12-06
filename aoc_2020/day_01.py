import math
from itertools import combinations
from _utils import *

inp = get_input(2020, 1)
nums = lmap(int, inp.strip().split("\n"))

# part 1
for t in combinations(nums, 2):
    if sum(t) == 2020:
        print(math.prod(t))

# part 2
for t in combinations(nums, 3):
    if sum(t) == 2020:
        print(math.prod(t))
