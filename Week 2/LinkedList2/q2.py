class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = None


def addEnd(head, val):
    newNode = Node(val)
    if(head == None):
        head = newNode
    else:
        temp = head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
    return head


def printLL(head):
    while(head != None):
        print(head.data, '->', end=" ")
        head = head.next
    print()


def checkPalindrome(head):
    # findling the middle slow will point
    slow = head
    fast = head
    while(True):
        if(fast == None or fast.next == None or fast.next.next == None):
            break
        else:
            slow = slow.next
            fast = fast.next.next
    # print(slow.data)
    # print(fast.data)

    # Slow is the mid
    # reverse the linkedlist after slow

    head1 = slow.next
    dummy = None
    next = None
    while(head1 != None):
        next = head1.next
        head1.next = dummy
        dummy = head1
        head1 = next
    slow.next = dummy
    printLL(head)
    print(slow.data)

    # checking for palindromes
    p1 = slow.next
    p2 = head
    while(p1 != None):
        if(p1.data != p2.data):
            return False
        p1 = p1.next
        p2 = p2.next
    return True


head = None
head = addEnd(head, 1)
head = addEnd(head, 2)
# head = addEnd(head, 1)
# head = addEnd(head, 3)
# head = addEnd(head, 4)
# head = addEnd(head, 5)
printLL(head)
print(checkPalindrome(head))
