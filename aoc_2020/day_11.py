import itertools

from _utils import *

inp = get_input(2020, 11)

seats = {}
for y, row in enumerate(inp.strip().split()):
    for x, v in enumerate(row):
        seats[(x, y)] = v


def step(seats, consider_func, min_occupied):
    for t, v in seats.items():
        adj = list(consider_func(seats, *t))
        if seats[t] == "L" and adj.count("#") == 0:
            yield t, "#"
        elif seats[t] == "#" and adj.count("#") >= min_occupied:
            yield t, "L"
        else:
            yield t, seats[t]


def evolve(seats, consider_func, min_occupied):
    prev = seats
    while (curr := dict(step(prev, consider_func, min_occupied))) != prev:
        prev = curr
    return curr


# part 1


def adjacent(seats, x, y):
    for t in itertools.product(range(x - 1, x + 2), range(y - 1, y + 2)):
        if (v := seats.get(t, None)) and t != (x, y):
            yield v


s1 = evolve(seats, adjacent, 4)
print(list(s1.values()).count("#"))


# part 2


def visible(seats, x, y):
    dirs = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
    ]
    for dx, dy in dirs:
        x_, y_ = x, y
        while vis := seats.get((x_ + dx, y_ + dy), None):
            yield vis
            if vis in ["L", "#"]:
                break
            x_, y_ = x_ + dx, y_ + dy


s2 = evolve(seats, visible, 5)
print(list(s2.values()).count("#"))
