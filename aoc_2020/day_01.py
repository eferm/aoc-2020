import math
from _utils import *

inp = get_input(2020, 1)
print(inp[:80])

nums = lmap(int, inp.strip().split("\n"))
print(nums)


# part 1
for i in range(len(nums)):
    j = len(nums) - 1
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(nums[i] * nums[j])

# part 2
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            items = [nums[i], nums[j], nums[k]]
            if sum(items) == 2020:
                print(math.prod(items))
