import itertools

from _utils import *

inp = get_input(2020, 9)
nums = lmap(int, inp.strip().split())

PRE = 25


def sums_to(x, seq, r=2):
    for t in itertools.combinations(seq, r):
        if sum(t) == x:
            return True
    return False


# part 1


def find_invalid():
    for i in range(PRE, len(nums)):
        if not sums_to(nums[i], nums[i - PRE : i]):
            return nums[i]


invalid = find_invalid()
print(invalid)

# part 2


def subseq(sum_to):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            seq = nums[i:j]
            if sum(seq) == invalid:
                return seq


s = subseq(invalid)
print(min(s) + max(s))
