import re
from _utils import *

inp = get_input(2020, 4)

passports = inp.strip().split("\n\n")
passports = lmap(lambda s: s.replace(" ", "\n"), passports)

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


# part 1


def validate1(passport):
    fields = [s[:3] for s in passport.split()]
    return len(set(fields).intersection(required)) == len(required)


valid = map(validate1, passports)
print(sum(valid))


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


def validate2(passport):
    res = map(lambda x: validators[x[:3]](x[4:]), passport.split())
    return sum(res) == len(required)


valid = map(validate2, passports)
print(sum(valid))
