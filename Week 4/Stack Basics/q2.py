def reverseString(s):
    stack = []
    for i in s:
        stack.append(i)
    new_string = []
    while(len(stack) > 0):
        new_string.append(stack.pop(-1))
    return ''.join(new_string)


a = 'Hello World'
print(reverseString(a))
