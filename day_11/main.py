with open('input.txt', 'r') as f:
    serial_number = int(f.read().strip())

grid = [[0] * 301 for _ in range(301)]


def init_grid(serial_number):
    for i in range(1, 301):
        for j in range(1, 301):

            rack_id = i + 10
            power_level = ((rack_id * j) + serial_number) * rack_id
            power_level = (power_level % 1000 // 100) - 5

            grid[i][j] = power_level + grid[i][j-1] + \
                grid[i-1][j] - grid[i-1][j-1]


def solve(b_size=1, e_size=301):
    subgrid_largest_power = 0
    top_left = (0, 0)
    subgrid_size = 0

    for size in range(b_size, e_size):
        for i in range(size, 301):
            for j in range(size, 301):

                subgrid_power = grid[i][j] + grid[i - size][j - size] - \
                    grid[i - size][j] - grid[i][j - size]

                if subgrid_power > subgrid_largest_power:
                    subgrid_largest_power = subgrid_power
                    top_left = (i - size + 1, j - size + 1)
                    subgrid_size = size

    return '{0},{1},{2}'.format(top_left[0], top_left[1], subgrid_size)


init_grid(serial_number)

first_part = solve(3, 4)
print('First part: {0}'.format(first_part))

second_part = solve()
print('Second part: {0}'.format(second_part))
