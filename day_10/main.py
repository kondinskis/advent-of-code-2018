import re
from collections import defaultdict


with open('input.txt', 'r') as f:
    points = [list(map(int, re.findall(r'-?\d+', line)))
              for line in f.read().splitlines()]


def move_points():
    global points

    for i in range(len(points)):
        points[i][0] += points[i][2]
        points[i][1] += points[i][3]


def check_multiples(points):
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    for posX, posY, _, _ in points:
        dic1[posX] += 1
        dic2[posY] += 1

    return max(dic1.values()) > 20 and max(dic2.values()) > 20


def solve():
    seconds = 0
    while not check_multiples(points):
        move_points()
        seconds += 1

    matrix = [['.'] * 220 for _ in range(220)]
    for posX, posY, _, _ in points:
        matrix[posY][posX] = '#'

    with open('output.txt', 'w') as f:
        for r in matrix:
            f.write('{0}\n'.format(''.join(r)))

    return seconds


second_part = solve()

print('First part: Check output.txt')
print('Second part: {0}'.format(second_part))
