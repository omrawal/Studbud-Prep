# reverse a stack using recursion
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

    def __str__(self) -> str:
        ans = 'top -> '
        # for i in self.stack:
        #     ans+str(i)+'\n'
        return ans+" "+str(self.stack)


def add_bottom(s, val):
    if(s.isEmpty()):
        s.push(val)
    else:
        temp = s.pop()
        add_bottom(s, val)
        s.push(temp)


def reverseStack(s):
    if(s.isEmpty()):
        return
    temp = s.pop()
    reverseStack(s)
    add_bottom(s, temp)


s = Stack()
print(s.isEmpty())
s.push(5)
s.push(10)
s.push(15)
# print(s.peek())
# print(s.pop())
# print(s.search(15))
# print(s.search(10))
# print(s.isEmpty())
print(s)
reverseStack(s)
print(s)
