def nextLargerElement(self, arr, n):
    # code here
    i = n-1
    ans = []
    stack = []
    while(i >= 0):
        if(len(stack) == 0):
            ans.append(-1)
        elif(len(stack) > 0 and stack[-1] > arr[i]):
            ans.append(stack[-1])
        elif(len(stack) > 0 and stack[-1] <= arr[i]):
            while(len(stack) > 0 and stack[-1] < arr[i]):
                stack.pop(-1)
            if(len(stack) == 0):
                ans.append(-1)
            else:
                ans.append(stack[-1])
        stack.append(arr[i])
        i -= 1
    return ans[::-1]
