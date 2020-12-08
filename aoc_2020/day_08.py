from operator import add, sub
from _utils import *


inp = get_input(2020, 8)
tape = inp.strip().split("\n")


def step(i, acc):
    op = {"+": add, "-": sub}
    instr, arg = tape[i].split()
    sign, num = arg[:1], arg[1:]
    if instr == "nop":
        i += 1
    elif instr == "acc":
        i += 1
        acc = op[sign](acc, int(num))
    elif instr == "jmp":
        i = op[sign](i, int(num))
    else:
        raise ValueError(i)
    return i, acc


def evaluate(tape, return_state_at_repeated):
    seen, i, acc = set(), 0, 0
    while i + 1 < len(tape):
        seen.add(i)
        i, acc = step(i, acc)
        if i in seen:
            return acc if return_state_at_repeated else None
    return acc


# part 1
print(evaluate(tape, True))

# part 2


def swaps(tape):
    for i in range(len(tape)):
        tape_ = list(tape)
        t = tape_.pop(i)
        instr, arg = t.split()
        if instr == "jmp":
            t = f"nop {arg}"
        elif instr == "nop":
            t = f"jmp {arg}"
        tape_.insert(i, t)
        yield tape_


for tape in swaps(tape):
    acc = evaluate(tape, False)
    if acc:
        print(acc)
