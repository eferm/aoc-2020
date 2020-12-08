from _utils import *


inp = get_input(2020, 8)
print(len(inp.split("\n")))
# inp = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""
tape = inp.strip().split("\n")
tape = list(enumerate(tape))
print(tape[:10])


def parse(instruction):
    return instruction.split()


acc = 0

i, instruction = tape[0]
seen = []

while True:
    if i in seen:
        break
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
    else:
        raise ValueError(i, instruction)

print(acc)
# for i, instruction in tape:
#     seen.append(i)

#     print(instruction)
