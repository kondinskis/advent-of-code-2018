import re

notes = {}

with open('input.txt', 'r') as f:
    data = f.read()
    initial_state_str = re.findall(
        r'^initial state:\s(.*)$', data, re.MULTILINE)[0]
    for note, next_gen in re.findall(
            r'^(.{5})\s\=\>.(.)$', data, re.MULTILINE):
        notes[note] = next_gen


def solve(generations):

    initial_state = list(initial_state_str)

    for i in range(2000):
        initial_state.insert(0, '.')
        initial_state.append('.')

    for i in range(generations):
        mark_for_change = []
        for index in range(2, len(initial_state) - 2):
            part = initial_state[index - 2:index + 3]
            key = ''.join(part)
            if key in notes:
                mark_for_change.append((index, key))

        for index, key in mark_for_change:
            initial_state[index] = notes[key]

    total = 0
    for index, pot in enumerate(initial_state):
        if pot == '#':
            total += (index - 2000)

    return total


def solve_part_2():
    generations_500 = solve(500)
    generations_499 = solve(499)
    return (50000000000 - 500) * \
        (generations_500 - generations_499) + generations_500


first_part = solve(20)
print('First part: {0}'.format(first_part))

second_part = solve_part_2()
print('Second part: {0}'.format(second_part))
