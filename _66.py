class NaturalList(list):

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer.')
        if value <= 0:
            raise ValueError('The value must be a natural number.')
        else:
            super().append(value)


integers = NaturalList()
integers.append(0)
print(integers)
