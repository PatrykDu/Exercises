class EmptyStackError(Exception):
    pass


class Stack:
    """The simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data[-1]


def transfer(stack_1, stack_2):
    for item in range(len(stack_1)):
        stack_2.push(stack_1.pop())
    return stack_1, stack_2


s1 = Stack()
s1.push('python')
s1.push('java')
s1.push('c++')

s2 = Stack()
s2.push('sql')

s1, s2 = transfer(s1, s2)
print(len(s1), len(s2))
