# check if number is palindrome


def reverseInt(n, temp=0):
    if(n == 0):
        return temp
    else:
        temp = (temp*10)+(n % 10)
        return reverseInt(n//10, temp)


def is_palindrome(n):
    if(n == 0):
        return True
    if(n < 0):
        return False
    reversed_n = reverseInt(n)
    if(reversed_n == n):
        return True
    else:
        return False


a = 112211
print(is_palindrome(a))
