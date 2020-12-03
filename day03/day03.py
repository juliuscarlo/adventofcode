# Day 03
# Part 1

import numpy as np

with open("input.txt") as file:
    data = [x.strip() for x in file.readlines()]

print(data)


def shift(word, n):
    n = n % len(word)
    return word[n:] + word[:n]


def count_trees(data, slope):
    n = 0
    count = 0
    for row in data:
        shifted_row = shift(row, n)
        n += slope
        if shifted_row[0] == '#':
            count += 1
    return count


answer = count_trees(data=data, slope=3)
print("answer: ")
print(answer)


# Part 2


def count_trees_special(data, slope):
    n = 0
    count = 0
    row_counter = 0
    for row in data:
        if row_counter % 2 == 1:
            pass
        else:
            shifted_row = shift(row, n)
            n += slope
            if shifted_row[0] == '#':
                count += 1

        row_counter += 1
    return count


factor = 1

for slope in [1, 3, 5, 7]:
    factor *= count_trees(data=data, slope=slope)
    print(factor)

print("with normal slopes: ")
print(factor)
print ("special slope.............")

factor *= count_trees_special(data=data, slope=1)

print("with special slope: ")
print(factor)
