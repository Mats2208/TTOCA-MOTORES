from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return False, None
        return True, self._items.popleft()

    def peek(self):
        if self.is_empty():
            return False, None
        return True, self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def get_size(self):
        return len(self._items)

    def print(self):
        for item in self._items:
            print(item)