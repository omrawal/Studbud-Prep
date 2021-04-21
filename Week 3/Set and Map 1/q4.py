def findbtimes(a, b):
    count_dict = dict()
    for i in a:
        if(i in count_dict):
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for i in count_dict:
        if(count_dict[i] == b):
            return i


a = [1, 1, 2, 2, 2, 3, 3, 3]
b = 2
print(findbtimes(a, b))
