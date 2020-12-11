""" Day 09"""


def import_data(filename):
    with open(filename) as f:
        data = f.readlines()
        data = [int(x.strip()) for x in data]
        return data


data = import_data(filename="input.txt")
print(data)


def valid_number(data, index, number):
    valid = False
    while not valid:
        candidates = data[index - 25:index]
        delta = [number - x for x in candidates]
        index_n = 0
        for n in delta:
            selection = candidates[:index_n] + candidates[index_n + 1:]
            for candidate in selection:
                if n - candidate == 0:
                    valid = True
                    return valid
                    print("test")
            index_n += 1
        if not valid:
            return valid


def analyze_stream(data):
    index = 25
    for number in data[25:]:
        if not valid_number(data, index, number):
            print(number)
            return False
        index += 1


answer = analyze_stream(data)
print(answer)

# Part 2
# find a contiguous range of numbers that adds up to 15353384 in the data, add up lower and upper bound

data = import_data(filename="input.txt")
print(data)


def find_range(data):
    low = 0
    high = 0
    expected = 15353384
    # expected = 127
    # set initial lower and upper bound (indices)
    l = 0
    h = 1
    searching = True

    while searching:
        if sum(data[l:h]) == expected:
            total1 = sum(data[l:h])
            searching = False
            print("BINGO!")
            series = data[l:h]
            series.sort()
            return series[0] + series[-1]
        while sum(data[l:h]) < expected:
            total2 = sum(data[l:h])
            h += 1
        if sum(data[l:h]) > expected:
            l += 1
        while sum(data[l:h]) > expected:
            h -= 1





answer2 = find_range(data)
print(answer2)
