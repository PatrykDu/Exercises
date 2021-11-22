import random


random.seed(10)


def generate_random_point():
    return random.uniform(-1, 1), random.uniform(-1, 1)


def is_in_unit_circle(point):
    return point[0] ** 2 + point[1] ** 2 <= 1


def estimate(amount):
    points = []
    for i in range(0, amount):
        points.append(generate_random_point())
    flags = []
    for point in points:
        flags.append(is_in_unit_circle(point))
    x = 0
    for flag in flags:
        if flag is True:
            x += 1
    return 4 * x/amount


print(estimate(10000))

