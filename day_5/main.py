import string

with open('input.txt', 'r') as f:
    polymer = f.read().strip()


def react(a, b):
    return a.lower() == b.lower() and \
        ((a.isupper() == b.islower()
          or a.islower() == b.isupper()))


def units_remain(polymer, skip_letter=None):
    stack = []
    for unit in polymer:
        if skip_letter == unit.lower():
            continue
        if stack and react(unit, stack[-1]):
            stack.pop()
        else:
            stack.append(unit)

    return len(stack)


def shortest_polymer(polymer):

    shortest = 50000
    for letter in string.ascii_letters:
        shortest = min(units_remain(polymer, letter), shortest)

    return shortest


first_part = units_remain(polymer)
print('First part: {0}'.format(first_part))

second_part = shortest_polymer(polymer)
print('Second part: {0}'.format(second_part))
