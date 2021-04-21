# check if c is combination of a,b
def checkInterleaving(a, b, c):
    i = 0
    j = 0
    k = 0
    a_len = len(a)
    b_len = len(b)
    c_len = len(c)

    while(k < c_len):
        if(i < a_len and a[i] == c[k]):
            i += 1
            k += 1
        elif(j < b_len and b[j] == c[k]):
            j += 1
            k += 1
        else:
            print('One')
            return False
    # while(i < a_len and k < c_len):
    #     if(a[i] == c[k]):
    #         i += 1
    #         k += 1
    #     else:
    #         print('Two')
    #         return False
    # while(j < b_len and k < c_len):
    #     if(b[j] == c[k]):
    #         j += 1
    #         k += 1
    #     else:
    #         print('Three')
    #         return False
    if(i < a_len-1 or j < b_len-1):
        return False
    return True


print(checkInterleaving(a="AB", b="CD", c="ACBG"))
