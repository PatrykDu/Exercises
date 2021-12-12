class Matrix:

    def __init__(self, array):

        if not isinstance(array, list):
            raise TypeError('To create a matrix you need to pass a nested list of values.')

        if len(array) != 0:
            if not all(isinstance(row, list) for row in array):
                raise TypeError('Each element of the array (nested list) must be a list.')

            if not all(len(row) for row in array):
                raise TypeError('Columns must contain at least one item.')

            column_length = len(array[0])

            if not all(len(row) == column_length for row in array):
                raise TypeError('All columns must be the same length.')

            if not all(type(number) in (int, float) for row in array for number in row):
                raise TypeError('The values must be of type int or float.')

            self.array = array
        else:
            self.array = []

    def __repr__(self):
        return str(self.array)

    @property
    def n_rows(self):
        return len(self.array)

    @property
    def n_cols(self):
        if len(self.array) == 0:
            return 0
        return len(self.array[0])

    @property
    def size(self):
        return self.n_rows, self.n_cols

    @property
    def is_square_matrix(self):
        return self.size[0] == self.size[1]

    def zero(self):
        array = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        return Matrix(array)

    def identity(self):
        if not self.is_square_matrix:
            return None
        array = [[1 if row == col else 0 for row in range(self.n_rows)] for col in range(self.n_cols)]
        return Matrix(array)

    def add_row(self, row, index=None):
        if not isinstance(row, list):
            raise TypeError('Value must be a list.')
        for item in row:
            if type(item) not in (int, float):
                raise TypeError('Elements of the row must be an int or float')
        if self.n_cols != len(row):
            raise ValueError('List must have the same amount of the elements as the other rows')
        if index is None:
            self.array.append(row)
        else:
            self.array = self.array[:index] + [row] + self.array[index:]



m = Matrix([[3, 1, 6], [5, 2, 6], [5, 2, 6]])
print(m)

m.add_row([5, 7, 3])
print(m)
