import random


# Set random seed here
random.seed(20)


def generate_random_point():
    return random.uniform(-1, 1), random.uniform(-1, 1)


points = []

for i in range(0, 15):
    points.append(generate_random_point())


def is_in_unit_circle(point):
    if point[0] ** 2 + point[1] ** 2 <= 1:
        return True
    else:
        return False


flags = []
for point in points:
    flags.append(is_in_unit_circle(point))

print(flags)
