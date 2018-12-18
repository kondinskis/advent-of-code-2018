landscape = []


def init_landscape():
    global landscape
    with open('input.txt', 'r') as f:
        landscape = [list(x) for x in f.read().splitlines()]


def count_neighbors(acre):
    trees = 0
    lumberyards = 0
    row, col = acre

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue

            new_row = row + i
            new_col = col + j

            if new_row < 0 or new_row > len(landscape) - 1 \
                    or new_col < 0 or new_col > len(landscape[0]) - 1:
                continue

            if landscape[new_row][new_col] == '|':
                trees += 1
            elif landscape[new_row][new_col] == '#':
                lumberyards += 1

    return trees, lumberyards


def total_resources_after(minutes):
    init_landscape()
    for _ in range(minutes):
        mark_for_change = []
        for i, row in enumerate(landscape):
            for j, col in enumerate(row):
                trees, lumberyards = count_neighbors((i, j))

                new_state = None

                if col == '.' and trees >= 3:
                    new_state = '|'
                elif col == '|' and lumberyards >= 3:
                    new_state = '#'
                elif col == '#':
                    new_state = '#' if trees >= 1 and lumberyards >= 1 else '.'

                if new_state:
                    mark_for_change.append((i, j, new_state))

        for x, y, acre in mark_for_change:
            landscape[x][y] = acre

    trees = 0
    lumberyards = 0
    for c in landscape:
        trees += c.count('|')
        lumberyards += c.count('#')

    return trees * lumberyards


def solve_part_2():
    """ repeats every 700 mins, starting from 600
    642, 325 - 600 min
    563, 314 - 700 min
    623, 341 - 800 min
    574, 303 - 900 min
    590, 331 - 1000 min
    617, 312 - 1100 min
    592, 305 - 1200 min """

    return total_resources_after((1000000000 % 700) + 700)


first_part = total_resources_after(10)
print('First part: {0}'.format(first_part))

second_part = solve_part_2()
print('Second part: {0}'.format(second_part))
