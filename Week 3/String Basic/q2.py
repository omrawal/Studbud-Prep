string = input()
count_dict = {}
for i in string:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
for i in count_dict:
    print('Number of Occurrence of {} is:{}'.format(i, count_dict[i]))
