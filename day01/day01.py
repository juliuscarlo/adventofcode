# Day 01
# Part 1
print("############ Part 1 #############")

with open("input.txt") as f:
    content = f.readlines()
print(content)

content = [x.strip() for x in content]
print(content)

content = [int(x) for x in content]
print(content)


def find_2020_doubles(numbers):
    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                return i, j


answer_1 = find_2020_doubles(numbers=content)
print(answer_1[0] * answer_1[1])

print("############ Part 2 #############")


# Part 2
def find_2020_triplets(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i, j, k


answer_2 = find_2020_triplets(numbers=content)
print(answer_2[0] * answer_2[1] * answer_2[2])
