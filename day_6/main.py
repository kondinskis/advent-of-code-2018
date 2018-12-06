import re
from collections import defaultdict


def man_dist(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


with open('input.txt', 'r') as f:
    coordinates = [(int(i[0]), int(i[1]))
                   for i in re.findall(r"^(\d+)\D+(\d+)$",
                                       f.read(), re.MULTILINE)]

max_x = 0
max_y = 0
min_x = 100
min_y = 100

for coordinate in coordinates:
    max_x = max(max_x, coordinate[0])
    max_y = max(max_y, coordinate[1])
    min_x = min(min_x, coordinate[0])
    min_y = min(min_y, coordinate[1])


def solve():
    global coordinates

    grid = [[-1 for x in range(max_x + 1)] for y in range(max_y + 1)]
    min_distances = defaultdict(lambda: 10001)
    region = 0

    for j in range(max_y + 1):
        for i in range(max_x + 1):
            sum_man_dist = 0
            for coordinate in enumerate(coordinates):
                dist = man_dist(coordinate[1], (i, j))
                sum_man_dist += dist

                coordinate_key = '{0}#{1}'.format(i, j)

                if min_distances[coordinate_key] > dist:
                    min_distances[coordinate_key] = dist
                    grid[j][i] = coordinate[0] + 1

                elif min_distances[coordinate_key] == dist:
                    min_distances[coordinate_key] = dist
                    grid[j][i] = -1

            if sum_man_dist < 10000:
                region += 1

    areas = []

    for coordinate in enumerate(coordinates):
        x, y = coordinate[1]
        coordinate_id = coordinate[0] + 1
        if x > min_x and x < max_x and y > min_y and y < max_y:
            area_size = 0
            for i in grid:
                area_size += i.count(coordinate_id)
            areas.append(area_size)

    return sorted(areas)[-2], region


first_part, second_part = solve()
print('First part: {0}'.format(first_part))
print('Second part: {0}'.format(second_part))
