def counting(a):
    count_dict = {}
    for i in a:
        if(i in count_dict):
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for i in count_dict:
        if(count_dict[i] == 2):
            return i
    return -1


def sum_method(a):
    n = len(a)
    exp_sum = n*(n-1)/2
    obs_sum = sum(a)
    return int(abs(obs_sum-exp_sum))


a = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
print(counting(a))
print(sum_method(a))
