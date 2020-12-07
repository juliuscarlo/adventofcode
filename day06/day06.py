""" Day 06 """

file = open("input.txt", "r")


def read_input(file):
    file = open("input.txt", "r")
    data = {}
    group_id = 0
    count = 0
    group_counter = 0
    for line in file:
        line = line.strip()
        if group_id not in data.keys():
            data[group_id] = str()
        if len(line) == 0:
            for char in set(data[group_id]):
                if data[group_id].count(char) == group_counter:
                    count += 1
            group_id += 1
            group_counter = 0
        else:
            data[group_id] = data[group_id] + line
            group_counter += 1
    # must add the last group manually, as file does not end with empty line
    for char in set(data[group_id]):
        if data[group_id].count(char) == group_counter:
            count += 1
    file.close()
    return count


answer = read_input(file=file)
print(answer)