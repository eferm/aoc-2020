from _utils import *

inp = get_input(2020, 5)
seats = inp.strip().split("\n")


def seat_id(seat):
    bits = translate({"F": "0", "B": "1", "L": "0", "R": "1"}, seat)
    return int(bits, 2)


ids = lmap(seat_id, seats)

# part 1
print(max(ids))

# part 2
it = iter(sorted(ids))
x = [(i + j) // 2 for i, j in zip(it, it) if i + 1 < j]
print(x.pop())
