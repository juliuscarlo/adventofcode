# Day 04
# Part 1

import numpy as np
import json

file = open("input.txt", "r")


def read_input(file):
    data = {}
    passport_index = 0
    for line in file:
        if passport_index not in data.keys():
            data[passport_index] = list()
        if len(line) == 1:
            passport_index += 1
        else:
            for entry in [x.strip() for x in line.split()]:
                data[passport_index].append(entry)
    return data


passports = read_input(file=file)


def all_fields_valid(passport_data):
    """ Returns True if all fields are valid"""
    valid = True
    for field in passport_data:
        key, value = field.split(":")
        print(key)
        print(value)
        if key == "byr":
            if not (len(value) == 4 and 1920 <= int(value) <= 2002):
                print("*")
                valid = False
        elif key == "iyr":
            if not (len(value) == 4 and 2010 <= int(value) <= 2020):
                print("*")
                valid = False
        elif key == "eyr":
            if not (len(value) == 4 and 2020 <= int(value) <= 2030):
                print("*")
                valid = False
        elif key == "hgt":
            if value[-2:] == "cm":
                if not (150 <= int(value[:-2]) <= 193):
                    print("*")
                    valid = False

            elif value[-2:] == "in":
                if not (59 <= int(value[:-2]) <= 76):
                    print("*")
                    valid = False
            else:
                print("*")
                valid = False
        elif key == "hcl":
            if not (value[0] == "#" and len(value) == 7 and (x in "0123456789abcdef" for x in value[1:])):
                print("*")
                valid = False
        elif key == "ecl":
            if not (value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                print("*")
                valid = False
        elif key == "pid":
            if not (len(value) == 9 and (x in "0123456789" for x in value)):
                print("*")
                valid = False
    print(valid)
    return valid


def count_valid_passports(passports=passports):
    count = 0
    for passport in range(len(passports.items())):
        _, passport_data = passports.popitem()
        print(passport_data)
        if len(passport_data) == 8:
            if all_fields_valid(passport_data):
                count += 1
            else:
                pass
        elif len(passport_data) == 7:
            if "cid" not in "".join(passport_data):
                if all_fields_valid(passport_data):
                    count += 1
                else:
                    pass
            else:
                pass

    return count


answer = count_valid_passports(passports)
print(answer)

# part 2
