class Node:
    def __init__(self, val, n):
        self.val = val
        self.next = n

#not all mwthods, check linkedlist file 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def addToHead(self, val):
        if self.size == 0:
            n = Node(val, None)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n = Node(val, self.head)
            self.head = n
            self.size += 1

    def remove_node(self, val):
        current_node = self.head

        if current_node.val == val:
            self.head = self.head.next
            self.size -= 1
            return

        while(current_node != None and current_node.next.val != val):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    def printll(self):
        temp = self.head
        print('->', end=" ")
        while temp != None:
            print(temp.val, ' -> ', end = " ")
            temp = temp.next
        print()

#directed unweighted
class ListRepresentation:
    def __init__(self, v):
        self.list = []
        for i in range(v):
            self.list.append(LinkedList())
    
    def add_edge(self, n1, n2): #o(1)
        self.list[n1].addToHead(n2)
    
    def delete_edge(self, n1, n2): #o(V)
        self.list[n1].remove_node(n2)
    
    def print_graph(self): #o(V^2)
        for i in self.list: #o(v)
            i.printll() #o(v)

G = ListRepresentation(5)
G.add_edge(0,1)
G.add_edge(3,2)
G.add_edge(4,3)
G.delete_edge(4,3)
G.print_graph()