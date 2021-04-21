def balancedParenthesis(s):
    stack = []
    for i in s:
        if(i == '[' or i == '(' or i == '{'):
            stack.append(i)
        elif(i == ']' and len(stack) > 0 and stack[-1] == '['):
            stack.pop(-1)
        elif(i == ')' and len(stack) > 0 and stack[-1] == '('):
            stack.pop(-1)
        elif(i == '}' and len(stack) > 0 and stack[-1] == '{'):
            stack.pop(-1)
        else:
            return False
    if(len(stack) == 0):
        return True
    else:
        return False


a = '[(])'
print(balancedParenthesis(a))
