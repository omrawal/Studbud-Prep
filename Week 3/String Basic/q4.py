string = input()
count_dict = {}
for i in string:
    if(i in count_dict):
        count_dict[i] += 1
    else:
        count_dict[i] = 1
found = False
for i in count_dict:
    if(count_dict[i] > 1):
        found = True
        print(i)
        break
if(not found):
    print('Element not found!')
