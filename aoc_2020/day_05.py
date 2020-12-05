from _utils import *

inp = get_input(2020, 5)
seats = inp.strip().split("\n")

# part 1
ids = []
for seat in seats:
    bits = translate(
        {
            "F": "0",
            "B": "1",
            "L": "0",
            "R": "1",
        },
        seat,
    )
    ids.append(int(bits, 2))

print(max(ids))

# part 2
it = iter(sorted(ids))
for i, j in zip(it, it):
    if i + 1 < j:
        print((i + j) // 2)
