import re

def convert_input(file):
    arr = []
    passport = ""
    for line in file:
        if line != "\n":
            line = re.sub("\s", " ", line)
            passport += line
        else:
            passport = passport.rstrip(" ")
            arr.append(passport)
            passport = ""
    if passport != "":
        arr.append(passport)
    return arr

def parse_lines(arr):
    plist = []
    for str in arr:
        mlist = re.findall("[a-z]{3}:[^ ]*", str)
        passport = dict()
        for attr in mlist:
            passport[attr[:3]] = attr[4:]
        plist.append(passport)
    return plist

def check_complete(dict):
    keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for k in keys:
        if k not in dict:
            return False
    return True

def check_valid(dict):
    if not re.match("^200[0-2]|19[2-9][0-9]$", dict["byr"]) \
        or not re.match("^20(1[0-9]|20)$", dict["iyr"]) \
        or not re.match("^20(2[0-9]|30)$", dict["eyr"]) \
        or not re.match("^1([5-8][0-9]|9[0-3])cm$|^(59|6[0-9]|7[0-6])in$", dict["hgt"]) \
        or not re.match("^#[0-9a-f]{6}$", dict["hcl"]) \
        or not re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", dict["ecl"]) \
        or not re.match("^[0-9]{9}$", dict["pid"]):
            return False
    return True

input_res = open("day04-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()

passports = convert_input(input_arr)
passports = parse_lines(passports)

for p in passports:
    if check_complete(p):
        p["valid"] = True
    else:
        p["valid"] = False

pcount = 0
for p in passports:
    if p["valid"]:
        pcount += int(check_valid(p))
        
print(pcount)
