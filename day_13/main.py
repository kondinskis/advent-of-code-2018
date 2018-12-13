from collections import defaultdict

backslash_dir = {'>': 'v', '<': '^', '^': '<', 'v': '>'}
forwardslash_dir = {'>': '^', '<': 'v', '^': '>', 'v': '<'}
intersect = {'>l': '^', '<l': 'v', '^l': '<', 'vl': '>',
             '>r': 'v', '<r': '^', '^r': '>', 'vr': '<'}
next_intersect = {'l': 's', 's': 'r', 'r': 'l'}

with open('input.txt', 'r') as f:
    tracks = list([list(x) for x in f.read().splitlines()])


class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.intersection = 'l'
        self.crashed = False

    def next_position(self):
        if self.direction == '>':
            self.y += 1

        elif self.direction == '<':
            self.y -= 1

        elif self.direction == '^':
            self.x -= 1

        elif self.direction == 'v':
            self.x += 1

        next = tracks[self.x][self.y]

        if next == '\\':
            self.direction = backslash_dir[self.direction]

        elif next == '/':
            self.direction = forwardslash_dir[self.direction]

        elif next == '+':
            if self.intersection != 's':
                self.direction = intersect[self.direction + self.intersection]
            self.intersection = next_intersect[self.intersection]

    def generate_key(self):
        return '{0}#{1}'.format(self.x, self.y)

    def __lt__(self, other):
        return self.x <= other.x and self.y <= other.y


def init_carts(tracks):
    carts = []

    for i, row in enumerate(tracks):
        for j, field in enumerate(tracks[i]):
            if field in ['^', 'v', '<', '>']:
                carts.append(Cart(i, j, field))

    return carts


def find_first_crash():

    carts = init_carts(tracks)

    while True:
        carts.sort()
        carts_positions = defaultdict(list)
        for cart in carts:
            crash_spot = (cart.y, cart.x)
            carts_positions[cart.generate_key()].append(cart)
            cart.next_position()
            cart_key = cart.generate_key()
            carts_positions[cart_key].append(cart)
            if len(carts_positions[cart_key]) == 2:
                return '{0},{1}'.format(crash_spot[0], crash_spot[1])


def count_not_crashed(carts):
    not_crashed = 0
    not_crashed_cart = None
    for cart in carts:
        if not cart.crashed:
            not_crashed += 1
            not_crashed_cart = cart
    return not_crashed_cart, not_crashed


def find_last_cart():

    carts = init_carts(tracks)

    while True:
        carts.sort()
        carts_positions = defaultdict(list)

        for cart in carts:
            if not cart.crashed:
                carts_positions[cart.generate_key()].append(cart)
                cart.next_position()
                cart_key = cart.generate_key()
                carts_positions[cart_key].append(cart)
                if len(carts_positions[cart_key]) == 2:
                    for cart in carts_positions[cart_key]:
                        cart.crashed = True

        not_crashed_cart, not_crashed = count_not_crashed(carts)
        if not_crashed == 1:
            return '{0},{1}'.format(not_crashed_cart.y, not_crashed_cart.x)


first_part = find_first_crash()
print('First part: {0}'.format(first_part))

second_part = find_last_cart()
print('Second part: {0}'.format(second_part))
