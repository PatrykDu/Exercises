class IntDict(dict):

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer')
        else:
            super().__setitem__(key, value)


integers = IntDict()
integers['one'] = 1
print(integers)
