import re

clay = set()
flowing = set()
still = set()
to_fall = set()
to_spread = set()
min_y = 99999
max_y = 0


def init():
    global min_y, max_y
    with open('input.txt') as f:
        for match in re.finditer(
                r'^(.).(\d+)....(\d+)..(\d+)$', f.read(), re.MULTILINE):
            axis, num1, num2, num3 = match.groups()
            num1 = int(num1)
            num2 = int(num2)
            num3 = int(num3)

            if axis == 'x':
                for y in range(num2, 1 + num3):
                    clay.add((num1, y))
                min_y = min(min_y, num2, num3)
                max_y = max(max_y, num2, num3)
            elif axis == 'y':
                for x in range(num2, 1 + num3):
                    clay.add((x, num1))
                min_y = min(min_y, num1)
                max_y = max(max_y, num1)


def spread_side(spread_from, off, clay, still, water):
    while spread_from not in clay:
        water.add(spread_from)
        new_spread_from = (spread_from[0], spread_from[1] + 1)
        if new_spread_from not in clay and new_spread_from not in still:
            return spread_from
        spread_from = (spread_from[0] + off, spread_from[1])
    return None


def spread(spread_from, clay, flowing, still):
    water = set()
    pos_left = spread_side(spread_from, -1, clay, still, water)
    pos_right = spread_side(spread_from, 1, clay, still, water)
    if not pos_left and not pos_right:
        still.update(water)
    else:
        flowing.update(water)
    return pos_left, pos_right


def fall(to_fall_from, ly, clay, flowing):
    while to_fall_from[1] < ly:
        new_to_fall_from = (to_fall_from[0], to_fall_from[1] + 1)
        if new_to_fall_from not in clay:
            flowing.add(new_to_fall_from)
            to_fall_from = new_to_fall_from
        elif new_to_fall_from in clay:
            return to_fall_from
    return None


def solve():
    init()
    to_fall.add((500, 0))
    while to_fall or to_spread:
        while to_fall:
            tf = to_fall.pop()
            res = fall(tf, max_y, clay, flowing)
            if res:
                to_spread.add(res)

        while to_spread:
            ts = to_spread.pop()
            rl, rr = spread(ts, clay, flowing, still)
            if not rr and not rl:
                to_spread.add((ts[0], ts[1] - 1))
            else:
                if rl:
                    to_fall.add(rl)
                if rr:
                    to_fall.add(rr)

    still_no = 0
    flowing_no = 0
    for water_x, water_y in still:
        if water_y >= min_y:
            still_no += 1

    for water_x, water_y in flowing.difference(still):
        if water_y >= min_y:
            flowing_no += 1

    return flowing_no + still_no, still_no


first_part, second_part = solve()
print('First part: {0}'.format(first_part))
print('Second part: {0}'.format(second_part))
