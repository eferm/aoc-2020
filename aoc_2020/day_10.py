from _utils import *


inp = get_input(2020, 10)
adapters = lmap(int, inp.strip().split())
adapters += [max(adapters) + 3]


# part 1


def diffs(curr, seq):
    i, seq_ = 0, sorted(seq)
    while i < len(seq_):
        yield seq_[i] - curr
        i, curr = i + 1, seq_[i]


d = list(diffs(0, adapters))
print(d.count(1) * d.count(3))


# part 2


def graph(seq, branch=3):
    return {s: [x for x in seq if s < x <= s + branch] for s in seq}


def dfs(counts, graph, u, t):
    if u == t:
        return 1
    if u not in counts:
        counts[u] = sum(dfs(counts, graph, c, t) for c in graph[u])
    return counts[u]


print(dfs({}, graph([0] + adapters), 0, max(adapters)))
