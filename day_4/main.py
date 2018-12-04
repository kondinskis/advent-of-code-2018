import re
from collections import defaultdict

records = []

with open('input.txt', 'r') as f:
    records = list(map(
        lambda x: re.findall(r'\w+', x)[:7],
        f.read().splitlines())
    )

    def record_key(item):
        year, month, day, hour, minute, fi, se = item
        return '{0}-{1}-{2}-{3}-{4}'.format(year, month, day, hour, minute)

    records.sort(key=record_key)

guards = defaultdict(lambda: [0]*60)


def init_guards():
    global guards

    guard = -1
    g_asleep = -1
    g_up = -1

    for year, month, day, hour, minute, f_arg, s_arg in records:
        if f_arg == 'Guard':
            guard = s_arg
            g_asleep = -1
            g_up = -1
        elif f_arg == 'falls':
            g_asleep = int(minute)
            g_up = -1
        elif f_arg == 'wakes':
            g_up = int(minute)

        if g_asleep != -1 and g_up != -1:
            for i in range(g_asleep, g_up):
                guards[guard][i] += 1


def solve():
    global guards
    most_minutes_asleep = 0
    most_frequently_asleep = 0

    first_part = 0
    second_part = 0

    for guard, minutes in guards.items():
        total_minutes_asleep = sum(minutes)
        freq_minute_asleep = max(minutes)

        if total_minutes_asleep > most_minutes_asleep:
            most_minutes_asleep = total_minutes_asleep
            first_part = int(guard) * minutes.index(freq_minute_asleep)

        if freq_minute_asleep > most_frequently_asleep:
            most_frequently_asleep = freq_minute_asleep
            second_part = int(guard) * minutes.index(freq_minute_asleep)

    return first_part, second_part


init_guards()
first_part, second_part = solve()
print('First part: {0}'.format(first_part))
print('Second part: {0}'.format(second_part))
