import re
from _utils import *

inp = get_input(2020, 4)
# print(inp[:80])


passports = inp.strip().split("\n\n")
passports = lmap(lambda s: s.replace(" ", "\n"), passports)

required = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
]

# part 1
valid = 0
for passport in passports:
    fields = [s[:3] for s in passport.split("\n")]
    if len(set(fields).intersection(required)) == len(required):
        valid += 1

print(valid)


# part 2
def validate_hgt(field):
    if match := re.compile(r"(\d{2,3})(\w+)").match(field):
        num, unit = match.groups()
        if unit == "cm" and 150 <= int(num) <= 193:
            return True
        if unit == "in" and 59 <= int(num) <= 76:
            return True
    return False


validators = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": validate_hgt,
    "hcl": lambda x: bool(re.match(r"#[0-9a-f]{6}", x)),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: bool(re.match(r"^\d{9}$", x)),
    "cid": lambda x: False,
}

valid = 0
for passport in passports:
    validated = lmap(lambda x: validators[x[:3]](x[4:]), passport.split("\n"))
    valid += 1 if sum(lmap(int, validated)) == len(required) else 0

print(valid)
