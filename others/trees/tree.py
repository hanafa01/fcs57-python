
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, value): #o(n)
        if self.root == None:
            self.root = Node(value)
        else:
            n = Node(value)
            temp = self.root
            added = False
            while not added:
                if value >= temp.value:
                    if temp.right == None:
                        temp.right = n
                        n.parent = temp
                        added = True
                    else:
                        temp = temp.right
                else:
                    if temp.left == None:
                        temp.left = n
                        n.parent = temp
                        added = True
                    else:
                        temp = temp.left

    def search(self, value): #o(n)  worst case because of skewed tree, avg o(logn)
        if self.root == None:
            return False
        return self.helpSearch(value, self.root)

    def helpSearch(self, value, currentNode):
        if currentNode == None:
            return False
        
        if currentNode.value == value:
            return True
        
        if value >= currentNode.value:
            return self.helpSearch(value, currentNode.right)
        else:
            return self.helpSearch(value, currentNode.left)
    
    def deleteRoot(self):
        #empty tree
        if self.root == None:
            return
        
        #one node only (no left nor right)
        if self.root.right == None and self.root.left == None:
            val = self.root.value
            self.root = None
            return val
        
        #no right child in root
        if self.root.right == None and self.root.left != None:
            val = self.root.value
            self.root = self.root.left
            return val

        #no left child in root        
        if self.root.right != None and self.root.left == None:
            val = self.root.value
            self.root = self.root.right
            return val
    
        #two children
        #here: get value to replace in the right side of the root, get left most, if the left, get that one step to the right
        current = self.root
        current = current.right

        while current.left != None:
            current = current.left
        
        #save the value you will delete
        val = self.root.value
        #replace the value of the root with the value of current
        self.root.value = current.value

        #establishing new connections to delete current
        if current.right != None: #cuurent has the right child
            parent_c = current.parent
            child_c = current.right
            if parent_c != self.root:
                parent_c.right = child_c
            else:
                child_c.parent = parent_c
                
            parent_c.left = child_c
        else:
            parent_c = current.parent
            if parent_c != self.root:
                parent_c.left = None
            else:
                parent_c.right = None
        return val

    def deleteNode(self, value_to_delete): #o(n)
        if self.root == None:
            return None
        if self.root.value == value_to_delete:
            self.deleteRoot()
        
        current = self.root
        while current != None and current.value != value_to_delete:
            if current.value > value_to_delete:
                current = current.left
            else:
                current = current.right
        
        if current == None:
            return None
        
        if current.right == None and current.left == None:
            parent_c = current.parent
            if current.value < parent_c.value:
                parent_c.left = None
            else:
                parent_c.right = None
        elif current.left != None and current.right == None:
            parent_c = current.parent
            left_c = current.left
            if current.value < parent_c.value:
                parent_c.left = left_c
                left_c.parent = parent_c
            else:
                parent_c.right = left_c
                left_c.parent = parent_c
        elif current.left == None and current.right != None:
            parent_c = current.parent
            right_c = current.right
            if current.value < parent_c.value:
                parent_c.left = right_c
                right_c.parent = parent_c
            else:
                parent_c.right = right_c
                right_c.parent = parent_c
        else:
            temp = current.right

            while temp.left != None:
                temp = temp.left
            
            current.value = temp.value

            if temp.right != None:
                parent_temp = temp.parent
                right_temp = temp.right
                parent_temp.left = right_temp
                right_temp.parent = parent_temp
            else:
                parent_temp = temp.parent
                parent_temp.left = None


def inOrder(n):
    if n == None:
        return 
    inOrder(n.left)
    print(n.value)
    inOrder(n.right)

def preOrder(n):
    if n == None:
        return 
    print(n.value)
    inOrder(n.left)
    inOrder(n.right)

def postOrder(n):
    if n == None:
        return 
    inOrder(n.left)
    inOrder(n.right)
    print(n.value)

b = BST()

b.add(10)
b.add(5)
b.add(4)
b.add(2)
b.add(1)
b.add(3)
b.add(22)
b.add(11)
b.add(12)

print(b.deleteNode(10))
print(b.root.value)
print(b.root.right.left.value)
# print(b.search(11))

# inOrder(b.root)
# print(b.root.left.left.left.right.value)