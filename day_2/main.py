from collections import defaultdict
from itertools import combinations

box_ids = []

with open('input.txt', 'r') as f:
    box_ids = f.read().splitlines()


def calculate_checksum(box_ids):
    two = 0
    three = 0

    for box_id in box_ids:

        letters = defaultdict(int)
        for letter in box_id:
            letters[letter] += 1

        letters_values = letters.values()

        if 2 in letters_values:
            two += 1

        if 3 in letters_values:
            three += 1

    return two * three


def common_letters(box_ids):
    total_letters = len(box_ids[0])

    for i, j in combinations(box_ids, 2):

        common_letters = []
        for k in range(total_letters):
            if i[k] == j[k]:
                common_letters.append(i[k])

        if len(common_letters) + 1 == total_letters:
            return ''.join(common_letters)


first_part = calculate_checksum(box_ids)
print('First part: {0}'.format(first_part))

second_part = common_letters(box_ids)
print('Second part: {0}'.format(second_part))
