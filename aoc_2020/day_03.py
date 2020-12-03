import math
from _utils import *

inp = get_input(2020, 3)
# print(inp[:80])
# print(len(inp))

lines = inp.strip().split("\n")
width = len(lines[0])

# preview
for line in lines[:10]:
    print(line)

# part 1
path = []
x = 0
for line in lines[1:]:
    x += 3
    path.append(line[x % width])

trees = lfilter("#".__eq__, path)
print(len(trees))

# part 2
lengths = []
for step_x, step_y in zip(
    [1, 3, 5, 7, 1],
    [1, 1, 1, 1, 2],
):
    x = 0
    path = []
    for line in lines[step_y::step_y]:
        x += step_x
        path.append(line[x % width])
    trees = lfilter("#".__eq__, path)
    lengths.append(len(trees))

print(math.prod(lengths))
