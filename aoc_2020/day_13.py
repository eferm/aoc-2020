import itertools
import math

from _utils import *

inp = get_input(2020, 13)

arr, buses = inp.strip().split()
arr = int(arr)
buses = [(i, int(b)) for i, b in enumerate(buses.split(",")) if b != "x"]


# part 1

dep, bus = min(((arr // b) * b + b, b) for _, b in buses)
print(bus * (dep - arr))


# part 2

curr, step, solved = 0, 1, 0
while solved < len(buses):
    # step through until solve an additional bus
    for t in itertools.count(curr, step):
        matches = [bus for i, bus in buses if (t + i) % bus == 0]
        if len(matches) > solved:
            # print(f"{t:16.0f}", "solved", matches)
            curr, step, solved = t, math.lcm(*matches), len(matches)
            break

print(curr)
