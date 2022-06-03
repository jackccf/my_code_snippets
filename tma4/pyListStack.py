#File Name: pyListStack.py
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self.items.pop()

    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def swap(self):
        if self.size() < 2:
            return
        temp = self.items[-1]
        self.items[-1] = self.items[-2]
        self.items[-2] = temp
    
    def print(self):
        for i in range(-1, -len(self.items) - 1, -1):
            print(self.items[i], end=' ')
        print()


