import re
from collections import defaultdict, deque

with open('input.txt', 'r') as f:
    no_players, last_marble = map(int, re.findall(r'\d+', f.read()))


def solve(no_players, last_marble):
    circle = deque([0, 2, 1])
    players = defaultdict(int)
    curr_player = 3

    for i in range(3, last_marble + 1):
        if i % 23 == 0:
            circle.rotate(7)
            val = circle.pop()
            circle.rotate(-1)
            players[curr_player] += (val + i)
        else:
            circle.rotate(-1)
            circle.append(i)

        curr_player = (curr_player + 1) % no_players

    return max(players.values())


first_part = solve(no_players, last_marble)
print('First part: {0}'.format(first_part))

second_part = solve(no_players, last_marble * 100)
print('Second part: {0}'.format(second_part))
