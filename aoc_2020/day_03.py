import math
from _utils import *

inp = get_input(2020, 3)

lines = inp.strip().split("\n")
width = len(lines[0])


def path(x_step, y_step):
    x = 0
    for line in lines[y_step::y_step]:
        x += x_step
        yield line[x % width]


# part 1
print(len(lfilter("#".__eq__, path(3, 1))))

# part 2
steps = zip(
    [1, 3, 5, 7, 1],
    [1, 1, 1, 1, 2],
)
lengths = [len(lfilter("#".__eq__, path(*step))) for step in steps]
print(math.prod(lengths))
