# insert at bottom of stack
class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if(len(self.stack) == 0):
            return None
        else:
            return self.stack.pop(-1)

    def peek(self):
        if(len(self.stack) == 0):
            return None
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def __str__(self) -> str:
        ans = '->'
        for i in self.stack:
            ans += ' '+str(i)
        return ans

    def addBotttom(self, val):
        new_stack = []
        while(len(self.stack) > 0):
            new_stack.append(self.stack.pop(-1))
        new_stack.append(val)
        while(len(new_stack) > 0):
            self.stack.append(new_stack.pop(-1))
        return True


stack = Stack()
print(stack)
stack.push(0)
print(stack)
stack.push(1)
print(stack)
stack.push(2)
print(stack)
stack.push(3)
print(stack)
stack.push(4)
print(stack)
stack.push(5)
print(stack)
stack.addBotttom(99)
print(stack)
print(stack.pop())
print(stack)
