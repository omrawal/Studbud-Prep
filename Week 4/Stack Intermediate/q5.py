# infix to postfix

# using only '(',')' as brackets


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


def infixToPostfix(infix):
    postfix = ''
    stack = Stack()
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = ['+', '-', '*', '/', '^']
    for i in infix:

        if(i == '('):
            stack.push(i)

        elif(i == ')'):

            while(not stack.isEmpty() and stack.peek() != '('):
                postfix += stack.pop()

            stack.pop()

        elif(i in operators):

            if(stack.isEmpty() or stack.peek() == '(' or precedence[i] > precedence[stack.peek()]):
                stack.push(i)
            else:
                while(not stack.isEmpty() and stack.peek() != '(' and precedence[stack.peek()] >= precedence[i]):
                    postfix += stack.pop()

                stack.push(i)
        else:

            postfix += i

    while(stack.isEmpty() == False):

        postfix += stack.pop()

    return postfix


def postfixToInfix(postfix):
    # infix = ''
    stack = Stack()
    operators = ['+', '-', '*', '/', '^']
    for i in postfix:
        if(i in operators):
            right = stack.pop()
            left = stack.pop()
            ans = '('+left+i+right+')'
            stack.push(ans)
        else:
            stack.push(i)
    return stack.pop()


def infixToPrefix(infix):
    prefix = ''
    stack = Stack()
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = ['+', '-', '*', '/', '^']
    reversed_infix = ''
    for i in infix[::-1]:
        if(i == '('):
            reversed_infix += ')'
        elif(i == ')'):
            reversed_infix += '('
        else:
            reversed_infix += i
    print(reversed_infix)

    for i in reversed_infix:
        if(i == '('):
            stack.push(i)

        elif(i == ')'):

            while(not stack.isEmpty() and stack.peek() != '('):
                prefix += stack.pop()

            stack.pop()

        elif(i in operators):

            if(stack.isEmpty() or stack.peek() == '(' or precedence[i] > precedence[stack.peek()]):
                stack.push(i)
            else:
                while(not stack.isEmpty() and stack.peek() != '(' and precedence[stack.peek()] >= precedence[i]):
                    prefix += stack.pop()

                stack.push(i)
        else:

            prefix += i

    print('after for loop', prefix)
    while(not stack.isEmpty()):
        prefix += stack.pop()

    print(prefix)
    return prefix[::-1]


# postfix_exp = 'abcd^e-fgh*+^*+i-'
# print(postfixToInfix(postfix_exp))
# infix_exp = 'a+b*(c^d-e)^(f+g*h)-i'
# # print(infixToPostfix(infix_exp))
infix_exp = '(a+b)*c-d+f'
print(infixToPrefix(infix_exp))
