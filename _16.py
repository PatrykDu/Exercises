class Matrix:
    """Simple Matrix class."""

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]


m = Matrix('3 4\n5 6')
print(m.matrix)

