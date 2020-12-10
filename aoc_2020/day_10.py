from _utils import *


inp = get_input(2020, 10)
# print(inp[:80])
# print(len(inp.strip().split("\n")))


adapters = lmap(int, inp.strip().split())
adapters = sorted(adapters)
adapters += [max(adapters) + 3]
# print(adapters)


jolt = 0
a = []
diffs = []

for i in range(max(adapters) + 1):
    if i in adapters:
        adapters.remove(i)
        a.append(i)
        diffs.append(i - jolt)
        jolt = i

print(a)
print(len([x for x in diffs if x == 1]) * len([x for x in diffs if x == 3]))