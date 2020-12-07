from _utils import *
from collections import defaultdict

inp = get_input(2020, 7)
# print(inp)
# inp = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags."""
# for i in inp.split("\n"):
#     print(i)

rules = inp.strip().split("\n")
rules = lmap(lambda s: s.replace(".", ""), rules)
rules = lmap(lambda s: s.replace(" bags", "").replace(" bag", ""), rules)
rules = [tuple(rule.split(" contain ")) for rule in rules]
rules = [(k, v.split(", ")) for k, v in rules]
# for r in rules:
#     print(r)

import re

graph = defaultdict(set)
for bag, contains in rules:
    contains = lmap(lambda s: re.sub(r"(\d{1} )", "", s), contains)
    for x in contains:
        graph[x].add(bag)

# print(graph["shiny gold"])


def dfs(adj, node, visited, depth):
    visited.add(node)
    for n in adj.get(node, set()):  # get() since adj[] would mutate dict
        if n not in visited:
            dfs(adj, n, visited, depth + 1)
    return visited


print(len(dfs(graph, "shiny gold", set(), 0)) - 1)
# visiteds = []
# for node in graph:
#     print(node)
#     visiteds.append(dfs(graph, node, set(), 0))


# # # print(visiteds)
# # for x in visiteds:
# #     if "shiny gold" in x:
# #         print(x)
