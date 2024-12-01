# print('a' * 6)

class Node:
    def __init__(self, val, next):
        self.value = val
        self.next = next

class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addToHead(self, val):
        if self.size == 0:
            n = Node(val, None)
            self.head = n
            self.tail = n
        else:
            n = Node(val, self.head)
            self.head = n
        
        self.size += 1

    def addToTail(self, val):
        if self.size == 0:
            n = Node(val, None)
            self.head = n
            self.tail = n
        else:
            n = Node(val, None)
            self.tail.next = n
            self.tail = n
        
        self.size += 1

    def deleteHead(self):
        if self.size == 0:
            return 
    
        self.head = self.head.next
        self.size -= 1
    
    def print(self):
        current = self.head

        while current != None:
            print(current.value, end=" ")
            current = current.next
    
    def deleteTail(self):
        
        if self.size == 0:
            return
        
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1

        
        c = self.head
        while c.next.next != None:
            c = c.next

        c.next = None
        self.tail = c
        

# l = LL()

# l.addToHead(3)
# l.addToHead(4)
# # l.deleteHead()
# l.addToHead(34)
# l.deleteTail()
# l.print()
class MatrixRep:
    def __init__(self):
        self.matrix = []
        self.nodes = []
        self.node_count = 0

    def addNode(self, v):
        if v in self.nodes:
            return 
        
        self.node_count += 1

        for n in self.matrix:
            n.append(0)
        
        self.matrix.append([0] * self.node_count)

    def addEdge(self, v1, v2):
        if v1 not in self.nodes or v2 not in self.nodes:
            return
        
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)

        self.matrix[index1][index2] = 1
        self.matrix[index2][index1] = 1

    def deleteNode(self, v):
        if v not in self.matrix:
            return 
        
        index = self.nodes.index(v)

        self.node_count -= 1

        self.nodes.remove(v)

        self.matrix.pop(index)

        for i in self.matrix:
            i.pop(index)

class NodeTree:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.right = None
        self.left = None

class BT:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root == None:
            n = NodeTree(val)
            self.root = n
            return
        
        added = False
        current = self.root

        while not added:
            if current.value <= val:
                #right
                if current.right == None:
                    n = NodeTree(val)
                    current.right = n
                    n.parent = current
                    added = True
                else:
                    current = current.right
            else:
                #left
                if current.left == None:
                    n = NodeTree(val)
                    current.left = n
                    n.parent = current
                    added = True
                else:
                    current = current.left

    def search(self, value):
        if self.root == None:
            return False
        
        return self._search(value, self.root)
    
    def _search(self, value, node):
        if node == None:
            return False
        
        if node.value == value:
            return True
        
        if node.value <= value:
            return self._search(value, node.right)
        else:
            return self._search(value, node.left)
    
    def deleteRoot(self):
        if self.root == None:
            return False

        if self.root.left == None and self.root.right == None:
            self.root = None

        if self.root.left and self.root.right == None:
            #nodes only in left 
            self.root = self.root.left
            return True
        
        if self.root.right and self.root.left == None:
            #nodes only in right 
            self.root = self.root.right
            return True
        
        #both childs
        #chose right side, so left most node
        current = self.root
        current = current.right
        while current.left != None:
            current = current.left

        self.root.value = current.value

        if current.right != None:
            
            p = current.parent
            c = current.right
            if p == self.root:
                p.right = c
                c.parent = p
            else:
                p.left = c
                c.parent = p
        else:
            p = current.parent
            p.left = None

        return True
    
    def deleteNode(self, val):
        if self.root == None:
            return False
        
        if val == self.root.value:
            return self.deleteRoot()
        
        current = self.root

        while current != None and current.value != val:
            if current.value <= val:
                current = current.right  
            else:
                current = current.left
        
        if current == None:
            return False
        
        if current.left == None and current.right == None:
            parent = current.parent
            if parent.value <= val:
                parent.right = None
            else:
                parent.left = None

        elif current.left and current.right == None:
            parent = current.parent
            lchild = current.left
            if parent.value <= val:
                parent.right = lchild
                lchild.parent = parent
            else:
                parent.left = lchild
                lchild.parent = parent

        elif current.right and current.left == None:
            parent = current.parent
            rchild = current.right
            if parent.value <= val:
                parent.right = rchild
                rchild.parent = parent
            else:
                parent.left = rchild
                rchild.parent = parent

        else:
            temp = current.right

            while temp.left != None:
                temp = temp.left
            
            current.value = temp.value
            
            if temp.right != None:
                p = temp.parent
                c = temp.right

                p.left = c
                c.parent = p
            else:
                p = temp.parent
                p.left = None

bt = BT()
bt.add(50)
bt.add(40)
bt.add(36)
bt.add(42)
bt.add(41)
bt.add(60)
bt.add(70)
bt.add(61)

bt.deleteNode(40)

print(bt.root.left.right.value)