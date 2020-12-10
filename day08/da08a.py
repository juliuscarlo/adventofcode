""" Day 8 (Part 2) """
with open("input.txt") as f:
    data = f.readlines()
    data = [x.strip().split() for x in data]
# print(data)
# print("xxx")
# print(data[0])

index = 0
accumulator = 0
visited = list()


# if index == len(data) -> program is terminated correctly. output the acc value.
def run(data_input):
    global accumulator
    global index
    global visited
    visited = list()
    accumulator = 0
    index = 0
    correctly_ended = False

    while index not in visited:
        if index == len(data):
            correctly_ended = True
            print(correctly_ended)
            print("last line +1 has been reached!")
            return accumulator, correctly_ended

        visited.append(index)
        operation, value = data[index]

        if operation == "acc":
            # print("adding to accumulator...")
            acc(value)
        elif operation == "jmp":
            # print("jumping...")
            jmp(value)
        elif operation == "nop":
            # print("doing nothing...")
            nop(value)

        print("::::: new index:::::")
        print(index)

        if index == len(data) + 1:
            correctly_ended = True
            print(correctly_ended)
            return accumulator, correctly_ended

        print("-------------------------")

    return accumulator, correctly_ended


def acc(value):
    global accumulator
    global index
    accumulator += int(value)
    index += 1


def jmp(value):
    global index
    index += int(value)


def nop(value):
    global index
    index += 1


print(data)


# Part 2
# try switching a nop to jmp and check if index ever reaches last instruction
def find_correction():
    for i in range(len(data)):
        current_data = data.copy()
        if data[i][0] == "jmp":
            current_data[i][0] = "nop"
            print("running program with switched operation...")
            result = run(data_input=current_data)
            # switch back the nop
            current_data[i][0] = "jmp"
            if result[1]:
                return result


answer = find_correction()
print(answer)
