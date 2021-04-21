# stack using Deque


class Deque(object):
    def __init__(self):
        self.deque = []
        self.dsize = 0

    def size(self):
        return self.dsize

    def isEmpty(self):
        if(self.size() == 0):
            return True
        else:
            return False

    def insertFront(self, val):
        self.deque.insert(0, val)
        self.dsize += 1

    def insertRear(self, val):
        self.deque.append(val)
        self.dsize += 1

    def removeFront(self):
        if(self.isEmpty()):
            return -1
        else:
            self.dsize -= 1
            return self.deque.pop(0)

    def removeRear(self):
        if(self.isEmpty()):
            return -1
        else:
            self.dsize -= 1
            return self.deque.pop(-1)


class Stack():
    def __init__(self):
        self.stack = Deque()

    def size(self):
        return self.stack.size()

    def isEmpty(self):
        return self.stack.isEmpty()

    def push(self, val):
        self.stack.insertRear(val)

    def pop(self):
        return self.stack.removeRear()


stk = Stack()
print(stk.push(7), 'Pushing 7')
print(stk.push(8), 'Pushing 8')
print(stk.pop(), 'Popping')
print(stk.pop(), 'Popping')
print(stk.pop(), 'Popping')
