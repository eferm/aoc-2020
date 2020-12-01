import math
from _utils import *

inp = get_input(2020, 1)
print(inp[:80])

nums = sorted(map(int, inp.strip().split("\n")))
print(nums)

# part 1
for i in range(len(nums)):
    j = len(nums) - 1
    while i < j and nums[i] + nums[j] > 2020:
        j -= 1
    if nums[i] + nums[j] == 2020:
        print(nums[i] * nums[j])

# part 2
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        k = len(nums) - 1
        while i < j < k and sum(x := [nums[i], nums[j], nums[k]]) > 2020:
            k -= 1
        if sum(x) == 2020:
            print(math.prod(x))
