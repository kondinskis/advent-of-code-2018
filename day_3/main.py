import re
from collections import defaultdict

claims = []

regex = r"^\#(\d*).{3}(\d*)\,(\d*).{2}(\d*).(\d*)$"

with open('input.txt', 'r') as f:
    claims = re.findall(regex, f.read(), re.MULTILINE)

fabric = defaultdict(int)


def fabric_two_or_more():
    global fabric
    for claim in claims:
        n, x, y, w, h = claim
        x = int(x)
        y = int(y)
        for i in range(1, int(w) + 1):
            for j in range(1, int(h) + 1):
                key = "{0}#{1}".format(x + i, y + j)
                fabric[key] += 1

    return len([x for x in fabric.values() if x > 1])


def find_intact():
    global fabric
    for claim in claims:
        n, x, y, w, h = claim
        x = int(x)
        y = int(y)

        is_claimed = False

        for i in range(1, int(w) + 1):
            for j in range(1, int(h) + 1):
                key = "{0}#{1}".format(x + i, y + j)
                if fabric[key] > 1:
                    is_claimed = True

        if not is_claimed:
            return n


first_part = fabric_two_or_more()
print('First part: {0}'.format(first_part))

second_part = find_intact()
print('Second part: {0}'.format(second_part))
