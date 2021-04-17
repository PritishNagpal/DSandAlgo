class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            curr_node = self.root
            while True:
                if data < curr_node.data:
                    if curr_node.left == None:
                        curr_node.left = new_node
                        return
                    else:
                        curr_node = curr_node.left
                elif data > curr_node.data:
                    if curr_node.right == None:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right

    def lookup(self,data):
        curr_node = self.root
        while True:
            if curr_node == None:
                return False
            if curr_node.data == data:
                return True
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

    def remove:
        if self.root == None:
            return False
        curr_node = self.root
        parent_node = None
        while True:
            if data < curr_node.data:
                parent_node = curr_node
                curr_node = curr_node.left
            elif data > curr_node.data:
                parent_node = curr_node
                curr_node = curr_node.right
            elif curr_node.data == data:

                if curr_node.right == None:
                    if parent_node == None:
                        self.root = curr_node.left
                    else:
                        # if parent value > current value, make current left child a child of parent
                        if curr_node.data < parent_node.data:
                            parent_node.left = curr_node.left
                        # if parent value < current value, make left child a right child of parent
                        elif curr_node.data > parent_node.data:
                            parent_node.right = curr_node.left
                # Option 2: Right child which does not have the left child
                elif(curr_node.right.left == None):
                    curr_node.right.left =  curr_node.left


# BINARY TREES
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def preOrder(root):
    #Write your code here
    if root is None:
        return
    else:
        print(root.info, end=" ")
        preOrder(root.left)
        preOrder(root.right)
        
def postOrder(root):
    #Write your code here
    if root is None:
        return
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=" ")

def inOrder(root):
    #Write your code here
    if root is None:
        return
    else:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)
