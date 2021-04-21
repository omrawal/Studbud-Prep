def eval_postfix(S):
    stack = []
    operator = ['+', '-', '*', '/']
    for i in S:
        if i in operator:

            if(i == '+'):
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                stack.append(a+b)

            elif(i == '-'):
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                stack.append(a-b)

            elif(i == '*'):
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                stack.append(a*b)

            elif(i == '/'):
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                stack.append(int(a//b))

        else:
            stack.append(i)
    return stack[-1]


s = "123+*8-"
print(eval_postfix(s))
