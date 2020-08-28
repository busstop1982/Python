from exceptions import Empty


class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()


if __name__ == '__main__':
    try:
        s = Stack()
        s.push(5)
        s.push(3)
        print(len(s))
        print(s.pop())
        print(s.is_empty())
        print(s.pop())
        print(s.is_empty())
        s.push(7)
        s.push(9)
        print(s.top())
        s.push(4)
        print(len(s))
        print(s.pop())
        s.push(6)
        s.push(8)
        while not s.is_empty():
            print(s.pop())
        print(s.pop())
    except Exception as msg:
        print(msg)
