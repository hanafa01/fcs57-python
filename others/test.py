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
        

l = LL()

l.addToHead(3)
l.addToHead(4)
l.deleteHead()
l.addToHead(34)
l.print()
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