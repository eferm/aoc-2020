import math
from operator import add, sub
from _utils import *


inp = get_input(2020, 12)
instructions = inp.strip().split()

dirs = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}


# part 1


def update_vec(vec, dir_, deg):
    # (E, R, 1) -> S
    op = {"L": sub, "R": add}
    compass = list(dirs.keys())
    new_vec = op[dir_](compass.index(vec), (deg / 90))
    return compass[int(new_vec) % 4]


def update_pos(pos, dir_, num):
    # ((0, 0), N, 1) -> (0, -1)
    dx, dy = dirs[dir_]
    return pos[0] + dx * num, pos[1] + dy * num


vec = "E"
pos = (0, 0)

for instr in instructions:
    dir_, num = instr[0], int(instr[1:])
    if dir_ in ["N", "E", "S", "W"]:
        pos = update_pos(pos, dir_, num)
    if dir_ in ["F"]:
        pos = update_pos(pos, vec, num)
    if dir_ in ["R", "L"]:
        vec = update_vec(vec, dir_, num)

print(abs(pos[0]) + abs(pos[1]))


# part 2


def update_rot(pnt, dir_, deg):
    # https://stackoverflow.com/a/34374437
    # ((1, 1), R, 90) -> (-1, 1)
    x, y = pnt
    angle = math.radians(deg if dir_ == "R" else 360 - deg)
    qx = math.cos(angle) * x - math.sin(angle) * y
    qy = math.sin(angle) * x + math.cos(angle) * y
    return round(qx), round(qy)


pos = (0, 0)
way = (10, -1)

for instr in instructions:
    dir_, num = instr[0], int(instr[1:])
    if dir_ in ["N", "E", "S", "W"]:
        way = update_pos(way, dir_, num)
    if dir_ in ["R", "L"]:
        way = update_rot(way, dir_, num)
    if dir_ in ["F"]:
        ew = "E" if way[0] > 0 else "W"
        ns = "S" if way[1] > 0 else "N"
        pos = update_pos(pos, ew, num * abs(way[0]))
        pos = update_pos(pos, ns, num * abs(way[1]))

print(abs(pos[0]) + abs(pos[1]))
