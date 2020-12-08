from _utils import *


inp = get_input(2020, 8)

tape = inp.strip().split("\n")
tape = list(enumerate(tape))


def evaluate(tape, break_infinite_loop):
    try:
        acc = 0
        i, instruction = tape[0]
        seen = []

        while True:
            if i in seen:
                return acc if break_infinite_loop else None

            seen.append(i)
            instr, arg = instruction.split()

            if instr == "nop":
                i, instruction = tape[i + 1]
            elif instr == "acc":
                sign, num = arg[:1], arg[1:]
                if sign == "+":
                    acc += int(num)
                elif sign == "-":
                    acc -= int(num)
                i, instruction = tape[i + 1]
            elif instr == "jmp":
                sign, num = arg[:1], arg[1:]
                if sign == "+":
                    i, instruction = tape[i + int(num)]
                elif sign == "-":
                    i, instruction = tape[i - int(num)]
    except IndexError:
        return acc


# part 1
print(evaluate(tape, True))

# part 2
tapes = []
for x in range(len(tape)):
    tape_ = list(tape)
    i, t = tape_.pop(x)
    instr, arg = t.split()
    if instr == "jmp":
        tape_.insert(x, (i, f"nop {arg}"))
    elif instr == "nop":
        tape_.insert(x, (i, f"jmp {arg}"))
    else:
        tape_.insert(x, (i, t))
    tapes.append(tape_)

for tape in tapes:
    acc = evaluate(tape, False)
    if acc:
        print(acc)
