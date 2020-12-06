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
x = [t for t in zip(it, it) if t[0] + 1 < t[1]]
print(sum(x.pop()) // 2)
