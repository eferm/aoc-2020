from _utils import *


def print_grid_dict(grid, charmap=None, default=0):
    # Expects a grid of (x, y) -> val
    # Charmap maps vals to tokens for printing.  Otherwise prints str(val).
    min_x = min([x for x, y in grid.keys()])
    max_x = max([x for x, y in grid.keys()])
    min_y = min([y for x, y in grid.keys()])
    max_y = max([y for x, y in grid.keys()])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            v = grid.get((x, y), default)
            if charmap:
                v = charmap[v]
            sys.stdout.write(str(v))
        sys.stdout.write("\n")


inp = get_input(2020, 11)
# inp = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""
# print(inp[:80])


def pr(m):
    for row in m:
        print("".join(row))


def flat(m):
    return [x for row in m for x in row]


seats = lmap(list, inp.strip().split())
# pr(seats)
# print(flat(seats))

X = len(seats[0])
Y = len(seats)
# print(X, Y)


def zone(x, y, seats):
    zone = seats[max(y - 1, 0) : min(y + 2, Y)]
    return [row[max(x - 1, 0) : min(x + 2, X)] for row in zone]


# pr(zone(0, 0, seats))
# pr(zone(9, 0, seats))
# pr(zone(0, 9, seats))
# pr(zone(9, 9, seats))

import copy


def occupy(m):
    to_occupy = []
    for y, row in enumerate(m):
        for x, v in enumerate(row):
            adjacent = flat(zone(x, y, m))
            if v == "L" and adjacent.count("#") == 0:
                to_occupy.append((x, y))
    n = copy.deepcopy(m)
    for x, y in to_occupy:
        n[y][x] = "#"
    return n


def empty(m):
    to_empty = []
    for y, row in enumerate(m):
        for x, v in enumerate(row):
            adjacent = flat(zone(x, y, m))
            if v == "#" and adjacent.count("#") > 4:
                to_empty.append((x, y))
    n = copy.deepcopy(m)
    for x, y in to_empty:
        n[y][x] = "L"
    return n


import itertools


def equals(m1, m2):
    eq = []
    for y in range(len(m1)):
        for x in range(len(m1[0])):
            eq.append(m1[y][x] == m2[y][x])
    return all(eq)


funcs = itertools.cycle([occupy, empty])


prev = list(seats)
curr = next(funcs)(prev)
# pr(prev)
# pr(curr)

while not equals(prev, curr):
    prev = curr
    curr = next(funcs)(curr)


print(flat(curr).count("#"))


# prev = list(seats)
# while prev != seats:
# for row in seats:
#     r = list(row)


# first_seat_empty = (i == 0) and (row[i + 1] in ["L", "."])
# mid_seat_empty = (0 < i < len(row) - 1) and (
#     (row[i - 1] in ["L", "."]) and (row[i + i] in ["L", "."])
# )
# last_seat_empty = (i == len(row) - 1) and (row[i - 1] in ["L", "."])
# if (
#     row[i] == "L"
#     and first_seat_empty
#     and mid_seat_empty
#     and last_seat_empty
# ):
#     return True
# return False
