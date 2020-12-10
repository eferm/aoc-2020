from _utils import *


inp = get_input(2020, 10)

adapters = lmap(int, inp.strip().split())
adapters = sorted(adapters) + [max(adapters) + 3]


# part 1


def diffs(curr, seq):
    for x in seq:
        yield x - curr
        curr = x


d = list(diffs(0, adapters))
print(d.count(1) * d.count(3))


# part 2


def graph(seq, branch=3):
    return {s: [x for x in seq if s < x <= s + branch] for s in seq}


def count(cache, graph, src, dst):
    if src == dst:
        return 1
    if src not in cache:
        cache[src] = sum(count(cache, graph, v, dst) for v in graph[src])
    return cache[src]


g = graph([0] + adapters)
print(count({}, g, 0, max(adapters)))
