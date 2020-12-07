import re
from collections import defaultdict
from _utils import *


inp = get_input(2020, 7)


def parse(rule):
    bag, targets = re.compile(r"(.+) bags contain (.+)").match(rule).groups()
    targets = [
        match.groups()
        for t in targets.split(", ")
        if (match := re.compile(r"(\d+) (.+) bag*").match(t))
    ]
    return bag, targets


rules = lmap(parse, inp.strip().split("\n"))


# part 1


def graph1(rules):
    graph = defaultdict(set)
    for bag, targets in rules:
        for num, target in targets:
            graph[target].add(bag)
    return graph


def traverse1(adj, node, visited):
    visited.add(node)
    for n in adj.get(node, set()):
        if n not in visited:
            traverse1(adj, n, visited)
    return visited


graph = graph1(rules)
print(len(traverse1(graph, "shiny gold", set())) - 1)


# part 2


def graph2(rules):
    graph = defaultdict(set)
    weights = {}
    for bag, targets in rules:
        for num, target in targets:
            graph[bag].add(target)
            weights[(bag, target)] = int(num)
    return graph, weights


def traverse2(adj, weights, node, mult):
    count = 0
    for neighbor in adj.get(node, set()):
        weight = weights[(node, neighbor)]
        count += weight + traverse2(adj, weights, neighbor, weight)
    return mult * count


graph, weights = graph2(rules)
print(traverse2(graph, weights, "shiny gold", 1))
