# reverse a string using recursion


def reverse(s):
    if(len(s) == 1):
        return s
    temp = s[-1]
    return (temp+reverse(s[:-1]))


a = 'Hello'
print(reverse(a))
