""" Day 8 """
with open("input.txt") as f:
    data = f.readlines()
    data = [x.strip().split() for x in data]
# print(data)
# print("xxx")
# print(data[0])

index = 0
accumulator = 0
visited = list()


def run():
    global accumulator
    while index not in visited:
        visited.append(index)
        operation, value = data[index]
        # print(operation)
        # print(value)

        if operation == "acc":
            # print("adding to accumulator...")
            acc(value)

        elif operation == "jmp":
            # print("jumping...")
            jmp(value)

        elif operation == "nop":
            # print("doing nothing...")
            nop(value)
    return accumulator


def acc(value):
    global accumulator
    global index
    accumulator += int(value)
    index += 1


def jmp(value):
    global index
    index += int(value)
    # print("new index:")
    # print(index)


def nop(value):
    global index
    index += 1




answer = run()
print(answer)

