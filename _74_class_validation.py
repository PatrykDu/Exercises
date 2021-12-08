class Matrix:

    def __init__(self, array):
        if not isinstance(array, list):
            raise TypeError('To create a matrix you need to pass a nested list of values.')
        if len(array) != 0:
            for item in array:
                if not isinstance(item, list):
                    raise TypeError('Each element of the array (nested list) must be a list.')
                if not len(item) == len(array[0]):
                    raise TypeError('All columns must be the same length')
                for number in item:
                    if not isinstance(number, (int, float)):
                        raise TypeError('The value must be of type int or float')

                self.array = array
        else:
            self.array = []

    def __repr__(self):
        return str(self.array)


matrix = Matrix([{5, 4}])
print(matrix)
