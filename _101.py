class Queue:
    """The simplest queue."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('The queue is empty.')
        return self._data.pop(0)

    def is_empty(self):
        if len(self._data) == 0:
            return True

    def first(self):
        return self._data[0]


que = Queue()
que.enqueue('529')
que.enqueue('512')
print(que.first())
