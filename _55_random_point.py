import random


def generate_random_point():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    return (x, y)


print(generate_random_point())
