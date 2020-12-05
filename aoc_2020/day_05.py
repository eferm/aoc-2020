from _utils import *

inp = get_input(2020, 5)
# print(inp[:80])

# inp = """BFFFBBFRRR
# FFFBBBFRRR
# BBFFBBFRLL
# """

seats = inp.strip().split("\n")
print(seats)

seat_ids = []

for seat in seats:
    x_half = 8
    y_half = 128
    print(seat)
    y_min, y_max = 0, 127
    # print(seat[:7], seat[7:])

    for y in seat[:7]:
        y_half = y_half // 2
        if y == "F":
            y_max -= y_half
        elif y == "B":
            y_min += y_half

    x_min, x_max = 0, 7
    for x in seat[7:]:
        x_half = x_half // 2
        if x == "R":
            x_min += x_half
        elif x == "L":
            x_max -= x_half

    row = y_min
    col = x_min

    # print(row, col)

    seat_ids.append(row * 8 + col)

print(max(seat_ids))
