class IntList(list):

    def append(self, object):
        if not isinstance(object, int):
            raise TypeError('The value must be an integer')
        else:
            super().append(object)


integers = IntList()
integers.append(3)
integers.append(40)
print(integers)
