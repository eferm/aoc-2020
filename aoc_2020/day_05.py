from _utils import *

inp = get_input(2020, 5)
seats = inp.strip().split("\n")

# part 1
ids = []
for seat in seats:
    y = seat[:7].replace("F", "0").replace("B", "1")
    x = seat[7:].replace("L", "0").replace("R", "1")
    ids.append(int(y, 2) * 8 + int(x, 2))

print(max(ids))

# part 2
it = iter(sorted(ids))
for i, j in zip(it, it):
    if i + 1 < j:
        print((i + j) // 2)
