# Circular Singly Linked List


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def createNode(val):
    temp = Node(val)
    return temp


def addend(val, head):
    newNode = createNode(val)
    if(head == None):
        head = newNode
        newNode.next = newNode
    else:
        temp = head
        temp = temp.next
        while(temp.next != head):
            temp = temp.next
        temp.next = newNode
        newNode.next = head
    return head


def addBeg(val, head):
    newNode = createNode(val)
    if(head == None):
        head = newNode
        newNode.next = newNode
    else:
        temp = head
        temp = temp.next
        while(temp.next != head):
            temp = temp.next
        temp.next = newNode
        newNode.next = head
        head = newNode
    return head


def search(key, head):
    temp = head
    if(temp.val == key):
        return True
    temp = temp.next
    while(temp != head):
        if(temp.val == key):
            return True
        temp = temp.next
    return False


def delNode(key, head):
    if(search(key, head) == False):
        return False
    else:
        temp = head
        if(temp.val == key):
            head = temp.next
            return head
        temp = temp.next
        while(temp != head):
            if(temp.next.val == key):
                temp.next = temp.next.next
                return head
            temp = temp.next


def print_cll(head):
    temp = head
    print(temp.val, '->', end=' ')
    temp = temp.next
    while(temp != head):
        print(temp.val, '->', end=' ')
        temp = temp.next
    print()


head = None
head = addend(1, head)
print('added 1')
head = addend(2, head)
print('added 2')
print_cll(head)
head = addend(3, head)
print('added 3')
print_cll(head)
head = addend(4, head)
print('added 4')
print_cll(head)

head = addBeg(7, head)
print('added 7')
print_cll(head)
head = addBeg(5, head)
print('added 5')
print_cll(head)
head = addBeg(6, head)
print('added 6')
print_cll(head)


head = delNode(1, head)
print('deleted 1')
print_cll(head)


head = delNode(2, head)
print('deleted 2')
print_cll(head)
