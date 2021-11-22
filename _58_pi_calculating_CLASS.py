import random


class MonteCarlo:

    def __init__(self, simulations):
        self.simulations = simulations

    @staticmethod
    def generate_random_point():
        return random.uniform(-1, 1), random.uniform(-1, 1)

    @staticmethod
    def is_in_unit_circle(point):
        if point[0] ** 2 + point[1] ** 2 <= 1:
            return True
        else:
            return False

    def estimate(self):
        points = []
        for i in range(0, self.simulations):
            points.append(self.generate_random_point())
        flags = []
        for point in points:
            flags.append(self.is_in_unit_circle(point))
        x = 0
        for flag in flags:
            if flag is True:
                x += 1
        return 4 * x / self.simulations


monte = MonteCarlo(10000)
print(monte.estimate())
