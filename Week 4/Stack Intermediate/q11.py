# reverse a stack without using loops
# idea is store values in function calls untill stack is empty

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

    def size(self):
        return len(self.stack)

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


def insert(stack, ele):
    if(stack.isEmpty()):
        stack.push(ele)
        # return stack
    else:
        temp = stack.peek()
        stack.pop()
        # stack = insert(stack, ele)
        insert(stack, ele)
        stack.push(temp)
        # return stack


def reverse(stack):
    if(stack.size() == 1):
        # return stack
        return
    else:
        temp = stack.peek()
        stack.pop()
        # stack = reverse(stack)
        reverse(stack)
        insert(stack, temp)
        # return stack


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s)
reverse(s)
print(s)
