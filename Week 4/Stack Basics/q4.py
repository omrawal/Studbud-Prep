# 2 stacks  in an array


class TwoStacks(object):
    def __init__(self, n):
        self.array = [None]*n
        self.top1 = -1
        self.top2 = n

    def pop1(self):
        if(self.top1 == -1):
            print('Stack Underflow')
        else:
            ans = self.array[self.top1]
            self.array[self.top1] = None
            self.top1 -= 1
            return ans

    def pop2(self):
        if(self.top2 == len(self.array)):
            print('Stack Underflow')
        else:
            ans = self.array[self.top2]
            self.array[self.top2] = None
            self.top2 += 1
            return ans

    def push1(self, val):
        if(self.top1 == self.top2):
            print('Stack Overflow')
        else:
            self.top1 += 1
            self.array[self.top1] = val

    def push2(self, val):
        if(self.top2 == self.top1):
            print('Stack Overflow')
        else:
            self.top2 -= 1
            self.array[self.top2] = val


ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))
