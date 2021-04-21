class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        k = self.stack.pop(-1)
        return k

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def search(self, k):
        return k in self.stack


s = Stack()
print(s.isEmpty())
s.push(5)
s.push(10)
s.push(15)
print(s.peek())
print(s.pop())
print(s.search(15))
print(s.search(10))
print(s.isEmpty())
