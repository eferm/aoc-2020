import copy
import itertools
from _utils import *


inp = get_input(2020, 11)

seats = {}
for y, row in enumerate(inp.strip().split()):
    for x, v in enumerate(row):
        seats[(x, y)] = v


seats = lmap(list, inp.strip().split())
X = len(seats[0])
Y = len(seats)


def flat(m):
    return [x for row in m for x in row]


def equals(m1, m2):
    eq = []
    for y in range(len(m1)):
        for x in range(len(m1[0])):
            eq.append(m1[y][x] == m2[y][x])
    return all(eq)


def adjacent(x, y, seats):
    rows = seats[max(y - 1, 0) : min(y + 2, Y)]
    return [row[max(x - 1, 0) : min(x + 2, X)] for row in rows]


def visible(x, y, seats):
    dirs = {
        "nw": (
            range(max(x - 1, -1), -1, -1),
            range(max(y - 1, -1), -1, -1),
        ),
        "n": (
            itertools.repeat(x),
            range(max(y - 1, -1), -1, -1),
        ),
        "ne": (
            range(min(x + 1, X), X),
            range(max(y - 1, -1), -1, -1),
        ),
        "e": (
            range(min(x + 1, X), X),
            itertools.repeat(y),
        ),
        "se": (
            range(min(x + 1, X), X),
            range(min(y + 1, Y), Y),
        ),
        "s": (
            itertools.repeat(x),
            range(min(y + 1, Y), Y),
        ),
        "sw": (
            range(max(x - 1, -1), -1, -1),
            range(min(y + 1, Y), Y),
        ),
        "w": (
            range(max(x - 1, -1), -1, -1),
            itertools.repeat(y),
        ),
    }
    v = []
    for k, ranges in dirs.items():
        for x_, y_ in zip(*ranges):
            val = seats[y_][x_]
            v.append(val)
            if val in ["L", "#"]:
                break
    return v


def occupy(m):
    to_occupy = []
    for y, row in enumerate(m):
        for x, v in enumerate(row):
            adjacent = visible(x, y, m)
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
            adjacent = visible(x, y, m)
            if v == "#" and adjacent.count("#") >= 5:
                to_empty.append((x, y))
    n = copy.deepcopy(m)
    for x, y in to_empty:
        n[y][x] = "L"
    return n


funcs = itertools.cycle([occupy, empty])
prev = list(seats)
curr = next(funcs)(prev)

while not equals(prev, curr):
    prev = curr
    curr = next(funcs)(curr)


print(flat(curr).count("#"))
