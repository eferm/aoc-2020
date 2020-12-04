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
valid_passports = 0
for passport in passports:
    valid = 0
    for field in passport.split("\n"):
        code, value = field[:3], field[4:]
        if code == "byr" and 1920 <= int(value) <= 2002:
            valid += 1
        elif code == "iyr" and 2010 <= int(value) <= 2020:
            valid += 1
        elif code == "eyr" and 2020 <= int(value) <= 2030:
            valid += 1
        elif code == "hgt":
            regex = re.compile(r"(\d{2,3})(\w+)")
            if match := regex.match(value):
                num, unit = match.groups()
                if unit == "cm" and 150 <= int(num) <= 193:
                    valid += 1
                elif unit == "in" and 59 <= int(num) <= 76:
                    valid += 1
        elif code == "hcl" and re.match(r"#[0-9a-f]{6}", value):
            valid += 1
        elif code == "ecl" and value in [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        ]:
            valid += 1
        elif code == "pid" and re.match(r"^\d{9}$", value):
            valid += 1

    if valid == len(required):
        valid_passports += 1

print(valid_passports)
