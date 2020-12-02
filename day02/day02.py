# Day 02
# Part 1

import numpy as np

print("############ Part 1 #############")

with open("input.txt") as f:
    data = f.readlines()
print(data)

data = [x.strip() for x in data]
print(data)


def valid_password(data):
    split = [x.split() for x in data]
    count = 0
    for line in range(len(data)):
        current_line = data[line].split()
        occurrence = 0
        print(current_line)
        print("xxx")
        lower, upper = current_line[0].split("-")
        print(lower)
        print(upper)
        rule_letter = current_line[1][0]
        print(rule_letter)
        password_letters = [char for char in current_line[2]]
        for letter in password_letters:
            if rule_letter == letter:
                occurrence += 1
                print("adding 1 to occurrence...")

        print(occurrence)
        if int(lower) <= occurrence <= int(upper):
            print("found one!")
            count += 1
    return count


answer = valid_password(data=data)
print(answer)

print("############ Part 2 #############")


def valid_password_2(data):
    count = 0
    for line in range(len(data)):
        current_line = data[line].split()
        first, second = [int(x) for x in (current_line[0].split("-"))]
        rule_letter = current_line[1][0]
        password = current_line[2]
        found_first = password[first-1] == rule_letter
        found_second = password[second-1] == rule_letter
        if found_first != found_second:
            count += 1

    return count


answer = valid_password_2(data=data)
print("answer:")
print(answer)