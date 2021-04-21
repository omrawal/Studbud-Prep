def remove_duplicate(s):
    a = set()
    for i in s:
        a.add(i)
    return ''.join(a)


s = input()
print(remove_duplicate(s))
