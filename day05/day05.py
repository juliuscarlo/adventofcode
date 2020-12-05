""" Day 05 """


def import_data():
    with open("input.txt") as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    data = [x.replace("F", "0") for x in data]
    data = [x.replace("B", "1") for x in data]
    data = [x.replace("L", "0") for x in data]
    data = [x.replace("R", "1") for x in data]
    return data


def convert_row_data(data):
    binary_row = [x[:-3] for x in data]
    decimal_row = [calculate_decimal(x) for x in binary_row]
    return decimal_row


def convert_col_data(data):
    binary_col = [x[-3:] for x in data]
    decimal_col = [calculate_decimal(x) for x in binary_col]
    return decimal_col


def calculate_decimal(x):
    decimal = 0
    for i in range(len(x)):
        j = len(x) - 1 - i
        decimal += (int(x[i])) * 2 ** j
    return decimal


def find_largest_product():
    data = import_data()
    row_numbers = convert_row_data(data)
    column_numbers = convert_col_data(data)
    seat_ids = [a * 8 + b for a, b in zip(row_numbers, column_numbers)]
    largest_seat_id = max(seat_ids)
    return largest_seat_id


answer = find_largest_product()
print(answer)


# Part 2

def find_my_seat():
    data = import_data()
    row_numbers = convert_row_data(data)
    column_numbers = convert_col_data(data)
    seat_ids = [a * 8 + b for a, b in zip(row_numbers, column_numbers)]
    seat_ids.sort()
    print(seat_ids)
    for seat in range(max(seat_ids) - min(seat_ids) - 1):
        if (seat_ids[seat] + seat_ids[seat + 1]) % 2 == 0:
            left_neighbor = seat_ids[seat]
    my_seat_id = left_neighbor + 1
    return my_seat_id


answer_2 = find_my_seat()
print(answer_2)
