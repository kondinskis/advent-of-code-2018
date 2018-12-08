from collections import defaultdict

with open('input.txt', 'r') as f:
    numbers = [int(num) for num in f.read().split()]


tree = defaultdict(list)

total = 0


def sum_metadata(entries):
    childs = entries[0]
    metadata = entries[1]

    entries = entries[2:]
    sum_entires = 0

    for i in range(childs):
        sum_node, entries = sum_metadata(entries)
        sum_entires += sum_node

    sum_entires += sum(entries[:metadata])

    return sum_entires, entries[metadata:]


def root_node_val(entries):
    childs = entries[0]
    metadata = entries[1]

    entries = entries[2:]
    child_nodes = []

    for i in range(childs):
        child_node_value, entries = root_node_val(entries)
        child_nodes.append(child_node_value)

    if childs == 0:
        return sum(entries[:metadata]), entries[metadata:]

    return sum(child_nodes[i - 1] for i in entries[:metadata]
               if 1 <= i <= len(child_nodes)), entries[metadata:]


first_part = sum_metadata(numbers)
print('First part: {0}'.format(first_part[0]))

second_part = root_node_val(numbers)
print('Second part: {0}'.format(second_part[0]))
