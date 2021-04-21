def getNthFromLast(head, n):
    # code here
    # front towards head
    front = head
    back = head
    count = 0
    while(back != None and count < n):
        count += 1
        back = back.next
    if(back == None and count < n):
        return -1
    else:
        while(back != None):
            front = front.next
            back = back.next
        return front.data
