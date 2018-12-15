with open('input.txt', 'r') as f:
    no_recipes = int(f.read().strip())


def ten_recipes_after(no_recipes):

    current = [0, 1]
    recipes = [3, 7]
    while len(recipes) < no_recipes + 10:

        next_recipe = recipes[current[0]] + recipes[current[1]]

        for dig in str(next_recipe):
            recipes.append(int(dig))

        current[0] = (current[0] + recipes[current[0]] + 1) % len(recipes)
        current[1] = (current[1] + recipes[current[1]] + 1) % len(recipes)

    return ''.join(map(str, recipes[-10:]))


def total_recipes_left(seq):

    current = [0, 1]
    recipes = [3, 7]
    while True:

        next_recipe = recipes[current[0]] + recipes[current[1]]

        for dig in str(next_recipe):
            recipes.append(int(dig))

            last_six = ''.join(map(str, recipes[-6:]))
            if last_six == str(seq):
                return len(recipes) - len(str(seq))

        current[0] = (current[0] + recipes[current[0]] + 1) % len(recipes)
        current[1] = (current[1] + recipes[current[1]] + 1) % len(recipes)


first_part = ten_recipes_after(no_recipes)
print('First part: {0}'.format(first_part))

second_part = total_recipes_left(no_recipes)
print('Second part: {0}'.format(second_part))
