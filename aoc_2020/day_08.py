from operator import add, sub
from _utils import *


inp = get_input(2020, 8)

tape = inp.strip().split("\n")
tape = list(enumerate(tape))


def step(i, instruction, acc):
    op = {"+": add, "-": sub}
    instr, arg = instruction.split()
    if instr == "nop":
        i += 1
    if instr == "acc":
        sign, num = arg[:1], arg[1:]
        i += 1
        acc = op[sign](acc, int(num))
    elif instr == "jmp":
        sign, num = arg[:1], arg[1:]
        i = op[sign](i, int(num))
    return *tape[i], acc


def evaluate(tape, return_state_at_repeated):
    seen = []
    i, instruction, acc = step(*tape[0], 0)
    while i + 1 < len(tape):
        if i in seen:
            return acc if return_state_at_repeated else None
        seen.append(i)
        i, instruction, acc = step(i, instruction, acc)
    return acc


# part 1
print(evaluate(tape, True))

# part 2


def swaps(tape):
    for i in range(len(tape)):
        tape_ = list(tape)
        _, t = tape_.pop(i)
        instr, arg = t.split()
        if instr == "jmp":
            t = f"nop {arg}"
        elif instr == "nop":
            t = f"jmp {arg}"
        tape_.insert(i, (i, t))
        yield tape_


for tape in swaps(tape):
    acc = evaluate(tape, False)
    if acc:
        print(acc)
