""" Day 07 """


def import_data():
    with open("input.txt") as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    data = [x.replace("bags.", "") for x in data]
    data = [x.replace("bag.", "") for x in data]
    data = [x.replace("bags", "") for x in data]
    data = [x.replace("bag", "") for x in data]
    data = [x.replace("contain", "") for x in data]
    data = [x.replace(",", "") for x in data]
    data = [x.replace("  ", " ") for x in data]
    data = [x.replace("  ", " ") for x in data]
    data = [x.strip() for x in data]
    return data


def extract_first_color(row):
    row_as_list = row.split()
    first_color = row_as_list[:2]
    first_color = "".join([x for x in first_color])
    rest_of_row = row_as_list[2:]
    return first_color, rest_of_row


def extract_contained_colors(rest_of_row):
    contained_colors = dict()
    term = rest_of_row
    for index in range(int(len(term) / 3)):
        amount = int(term[3 * index + 0])
        color_part1 = term[3 * index + 1]
        color_part2 = term[3 * index + 2]
        color = color_part1 + color_part2
        contained_colors[color] = amount
    return contained_colors


def make_color_rules(data):
    rules = dict()
    for row in data:
        first_color, rest_of_row = extract_first_color(row)
        if first_color not in rules.keys():
            rules[first_color] = extract_contained_colors(rest_of_row)
        else:
            print("CHECK IF SOMETHING TODO HERE")
    return rules


def find_golden_bag_parents():
    # start with the gold bags
    parents_of_gold_bags = None
    collection = set()
    parents_of_gold_bags = set()
    rules = make_color_rules(data=import_data())
    for parent, kids in rules.items():
        for color, freq in kids.items():
            if color == 'shinygold':
                collection.add(parent)
                parents_of_gold_bags.add(parent)
    # now go backwards from here
    while len(collection) > 0:
        popped_color = collection.pop()
        for parent, kids in rules.items():
            for color, freq in kids.items():
                if color == popped_color:
                    collection.add(parent)
                    parents_of_gold_bags.add(parent)
    return len(parents_of_gold_bags)


answer1 = find_golden_bag_parents()
print(answer1)

rules = make_color_rules(data=import_data())
print(rules)

level = 0

def fc(color, count):
    global level
    children = list()
    level += 1
    print("level:")
    print(level)
    for key, value in rules[color].items():
        children.append((key, value))
        print(children)
    if len(children) == 0:
        print("empty bag................. Value added:")
        print(count)
        return count
    else:
        print("checking child node...")
        print("level:::::::::::")
        print(level)
        print(count)
        return count + count * sum([fc(child[0], child[1]) for child in children])


answer2 = fc(color="shinygold", count=1) - 1
print(answer2)
print(rules)