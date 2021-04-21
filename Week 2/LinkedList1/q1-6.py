# Singly Linked List


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def createNode(val):
    node_obj = Node(val)
    return node_obj


def addNodeAtBeg(val, head):
    node = createNode(val)
    if(head == None):
        head = node
    else:
        node.next = head
        head = node
    return head


def addNodeAtEnd(val, head):
    node = createNode(val)
    if(head == None):
        head = node
    else:
        temp = head
        while(temp.next != None):
            temp = temp.next
        temp.next = node
    return head


def length(head):
    count = 0
    temp = head
    while(temp != None):
        count += 1
        temp = temp.next
    return count


def print_ll(head):
    temp = head
    while(temp != None):
        print(temp.val, '->', end=' ')
        temp = temp.next
    print()


def search(key, head):
    temp = head
    found = False
    while(temp != None):
        if(temp.val == key):
            found = True
            break
        temp = temp.next
    return found


def delete(key, head):
    res = search(key, head)
    if(res == False):
        return False
    else:
        temp = head
        if(head.val == key):
            head = head.next
            return head
        else:
            while(temp != None):
                if(temp.next.val == key):
                    nextNode = temp.next.next
                    temp.next = nextNode
                    break
                temp = temp.next
            return head


def nthnode(head, n):

    count = 1
    if(length(head) < n):
        return False
    else:
        temp = head
        while(temp != None):
            if(count == n):
                return temp.val
            count += 1
            temp = temp.next


def countValues(head):
    temp = head
    count_dict = {}
    while(temp != None):
        if(temp.val in count_dict):
            count_dict[temp.val] += 1
        else:
            count_dict[temp.val] = 1
        temp = temp.next

    return count_dict


def getMin(head):
    temp = head
    if(head == None):
        return False
    else:
        min_val = temp.val
        while(temp != None):
            min_val = min(min_val, temp.val)
            temp = temp.next
        return min_val


def getMax(head):
    temp = head
    if(head == None):
        return False
    else:
        max_val = temp.val
        while(temp != None):
            max_val = max(max_val, temp.val)
            temp = temp.next
        return max_val


head = None
head = addNodeAtBeg(0, head)
print('length is', length(head))
head = addNodeAtEnd(1, head)
print_ll(head)
print('length is', length(head))
head = addNodeAtBeg(-1, head)
print_ll(head)
print('length is', length(head))
head = addNodeAtEnd(2, head)
print_ll(head)
print('length is', length(head))

print('search 5', search(5, head))
print('search 2', search(2, head))
print('search -1', search(-1, head))

temp = delete(5, head)
if(temp != False):
    head = temp
print('delete 5 done')

print_ll(head)
print('length is', length(head))

temp = delete(0, head)
if(temp != False):
    head = temp

print('delete 0 done')

print_ll(head)
print('length is', length(head))

temp = delete(-1, head)
if(temp != False):
    head = temp

print('delete -1 done')

print_ll(head)
print('length is', length(head))

head = addNodeAtBeg(0, head)
print_ll(head)
print('length is', length(head))


head = addNodeAtBeg(-1, head)
print_ll(head)
print('length is', length(head))

head = addNodeAtEnd(-1, head)
print_ll(head)
print('length is', length(head))

head = addNodeAtEnd(0, head)
print_ll(head)
print('length is', length(head))

print('4 th node', nthnode(head, 4))
print('1 th node', nthnode(head, 1))
print('3 th node', nthnode(head, 3))
print('2 th node', nthnode(head, 2))
print('8 th node', nthnode(head, 8))

print(countValues(head))
print(getMin(head))
print(getMax(head))
