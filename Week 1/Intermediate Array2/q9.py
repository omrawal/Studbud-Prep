def first_non_repeating(arr):
    for i in arr:
        if(i in count_dict):
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for i in count_dict:
        if(count_dict[i] == 1):
            return i


arr = list(map(int, input().split()))
count_dict = {}
print(first_non_repeating(arr))
