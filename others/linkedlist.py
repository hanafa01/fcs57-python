class Node:
    def __init__(self, val, n):
        self.val = val
        self.next = n
    
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

    def addToTail(self, val):
        if self.size == 0:
            n = Node(val, None)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n = Node(val, None)
            self.tail.next = n
            self.tail = n
            self.size += 1

    def insert_at(self, pos, val):
        if pos < 0:
            return 'Postion should be greater than 0'
        
        if self.head == None:
            return 'LinkedList empty'
        
        if pos == 0:
            n = Node(val, self.head)
            self.head = n
            self.size += 1
            return 'Inserted'
        
        c = 0
        current_node = self.head
        while current_node != None and c+1 != pos:
            c = c + 1
            current_node = current_node.next
        
        if current_node != None:
            n = Node(val, current_node.next)
            current_node.next = n
            self.size += 1
            return 'Inserted'
        else:
            return 'Position not present'


    def remove_at(self, index):
        if self.head == None or index < 0:
            return 

        current_node = self.head
        position = 0

        if position == index:  
            # if self.size == 1:
            #     self.head = None
            # else:
            self.head = current_node.next   
            self.size -= 1
        else:
            while current_node != None and position+1 != index:
                current_node = current_node.next
                position += 1

            if current_node != None:
                current_node.next = current_node.next.next
                self.size -= 1
            else:
                print('Index not present')    
            
    def remove_node(self, val):
        current_node = self.head

        if current_node.val == val:
            # self.remove_first_node()
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
        while temp != None:
            print(temp.val, ' -> ', end = " ")
            temp = temp.next
        print()

    def get_length(self):
        if self.head == None:
            return 0

        c = 0
        current_node = self.head
        while current_node != None:
            c += 1
            current_node = current_node.next
        return c

ll = LinkedList()

ll.addToHead(1)
# ll.addToHead(2)
# ll.addToHead(3)
# ll.addToHead(4)

ll.printll()
print()

# ll.insert_at(2, 14)
# ll.printll()
# print()

ll.remove_at(0)
ll.printll()
print()