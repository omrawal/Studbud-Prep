class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree(object):

    def __init__(self):
        self.root = None

    def insertNode(self, val):
        new_node = Node(val)
        if(self.root == None):
            self.root = new_node
        else:
            temp = self.root
            while(temp.left != None and temp.right != None):
                if(val < temp.data):
                    if(temp.left == None):
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if(temp.right == None):
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right
            if(val < temp.data and temp.left == None):
                temp.left = new_node
                return
            elif(val >= temp.data and temp.right == None):
                temp.right = new_node
                return


def search(root, val):
    while(True):
        if(root == None):
            return False
        else:
            if(root.data == val):
                return True
            elif(root.data < val):
                if(root.right == None):
                    return False
                else:
                    root = root.right
            elif(root.data > val):
                if(root.left == None):
                    return False
                else:
                    root = root.left
            else:
                return False


def delete(root, val):
    if search(root, val):
        pass
    else:
        return False


def inorder_rec(root):
    if root == None:
        return
    else:
        inorder_rec(root.left)
        print(root.data)
        inorder_rec(root.right)


def preorder_rec(root):
    if(root == None):
        return
    else:
        print(root.data)
        preorder_rec(root.left)
        preorder_rec(root.right)


def postorder_rec(root):
    if(root == None):
        return
    else:
        postorder_rec(root.left)
        postorder_rec(root.right)
        print(root.data)


tree = Tree()
tree.insertNode(20)
tree.insertNode(10)
tree.insertNode(30)
tree.insertNode(5)
tree.insertNode(40)
inorder_rec(tree.root)
print('Search for 5 ', search(tree.root, 5))
print('Search for 15 ', search(tree.root, 15))
print('Search for 50 ', search(tree.root, 50))
print('Search for -10 ', search(tree.root, -10))
