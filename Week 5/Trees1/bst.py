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


def inorder_rec(root):
    if root == None:
        return
    else:
        inorder_rec(root.left)
        print(root.data)
        inorder_rec(root.right)


tree = Tree()
tree.insertNode(20)
tree.insertNode(10)
tree.insertNode(30)
tree.insertNode(5)
tree.insertNode(40)
inorder_rec(tree.root)
