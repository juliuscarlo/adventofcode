""" Day 10"""


def import_data(filename):
    with open(filename) as f:
        data = f.readlines()
        data = [int(x.strip()) for x in data]
        return data


data = import_data(filename="input.txt")
print(data)


def find_adapters(data):
    data.sort()
    print(data)
    adapter_sequence = list()
    jolt = 0
    ones = 0
    twos = 0
    threes = 0
    for j in data:
        print("j:")
        print(j)
        if j == jolt + 1:
            adapter_sequence.append((j, 1))
            jolt += 1
            ones += 1

        if j == jolt + 2:
            adapter_sequence.append((j, 2))
            jolt += 2
            twos += 1

        if j == jolt + 3:
            adapter_sequence.append((j, 3))
            jolt += 3
            threes += 1
    # remember final adapter, so +3 jolts!
    jolt += 3
    adapter_sequence.append((jolt, 3))
    threes += 1
    print(ones)
    print(threes)
    return ones * threes


answer = find_adapters(data=data)
print(answer)

