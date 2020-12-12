import math
from operator import add, sub
from _utils import *


inp = get_input(2020, 12)
instructions = inp.strip().split()

dirs = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


# part 1


def update_vec(curr, dir_, deg):
    op = {"L": sub, "R": add}
    compass = list(dirs)
    return compass[int(op[dir_](compass.index(curr), (deg / 90)) % 4)]


def update_pos(curr, dir_, num):
    dx, dy = dirs[dir_]
    return curr[0] + (dx * num), curr[1] + (dy * num)


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


def update_dir(curr, dir_, num):
    dx, dy = dirs[dir_]
    return curr[0] + (dx * num), curr[1] + (dy * num)


def update_rot(ship, curr, dir_, num):
    ox, oy = ship
    px, py = curr
    angle = math.radians(num if dir_ == "R" else 360 - num)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return round(qx), round(qy)


pos = (0, 0)
way = (10, -1)


for instr in instructions:
    print(instr)
    dir_, num = instr[0], int(instr[1:])
    if dir_ in ["N", "E", "S", "W"]:
        way = update_dir(way, dir_, num)
    if dir_ in ["R", "L"]:
        way = update_rot((0, 0), way, dir_, num)
    if dir_ in ["F"]:
        ew = "E" if way[0] > 0 else "W"
        ns = "S" if way[1] > 0 else "N"
        pos = update_dir(pos, ew, num * abs(way[0]))
        pos = update_dir(pos, ns, num * abs(way[1]))

print(abs(pos[0]) + abs(pos[1]))
