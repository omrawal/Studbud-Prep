def s1substrings2(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    i = 0  # points s1
    j = 0  # points s2
    while(j < s2_len and i < s1_len):
        if(s1[i] == s2[j]):
            i += 1
            j += 1
        else:
            j += 1
    if(i == s1_len):
        return True
    else:
        return False


def checkRotation(s1, s2):
    temp = s1+s1
    if(s1substrings2(s2, temp)):
        return True
    else:
        return False


# print(checkRotation('AACD', 'ACDA'))
print(s1substrings2('afg', 'garfaafgjtnafgafg'))
