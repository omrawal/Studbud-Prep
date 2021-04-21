def reverseList(self, head):
    # Code here
    dummy = None
    next = None
    while(head != None):
        next = head.next
        head.next = dummy
        dummy = head
        head = next
    return dummy
