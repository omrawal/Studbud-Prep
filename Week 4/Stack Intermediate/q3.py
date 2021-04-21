# min stack time O(1) and O(1) space


class Stack(object):
    def __init__(self):
        self.stack = []
        self.minEle = None

    def getMin(self):
        return self.minEle

    def peek(self):
        if(len(self.stack) == 0):
            return -1
        else:
            top = self.stack[-1]
            if(top >= self.minEle):
                return top
            else:
                return self.minEle

    def push(self, val):
        if(len(self.stack) == 0):
            self.stack.append(val)
            self.minEle = val
        else:
            if(val >= self.minEle):
                self.stack.append(val)
            elif(val < self.minEle):
                self.stack.append(2*val-self.minEle)
                self.minEle = val

    def pop(self):
        if(len(self.stack) == 0):
            return -1
        else:
            top = self.peek()
            if(top >= self.minEle):
                self.stack.pop(-1)
                return top
            elif(top < self.minEle):
                self.minEle = 2*self.minEle-top
                self.stack.pop(-1)
                return top


# s = Stack()
# s.push(5)
# s.push(10)
# s.push(3)
# print(s.pop())
# print(s.pop())
# print(s.pop())

stack = Stack()

print(stack.push(3), 'pushed 3')
print(stack.push(5), 'pushed 5')
print(stack.getMin(), 'is min')
print(stack.push(2), 'pushed 2')
print(stack.push(1), 'pushed 1')
print(stack.getMin(), 'is min')
print(stack.pop(), 'is popped')
print(stack.getMin(), 'is min')
print(stack.pop(), 'is popped')
print(stack.peek(), 'is top')
