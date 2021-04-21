def removeDuplicateWords(a):
    word_list = a.split(' ')
    word_set = set()
    for i in word_list:
        word_set.add(i)
    return ' '.join(word_set)


a = "Geeks for Geeks A Computer Science portal for Geeks"
print(removeDuplicateWords(a))
