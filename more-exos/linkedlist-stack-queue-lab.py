class Node:
    def __init__(self, val, n):
        self.val = val
        self.next = n

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.isEmpty():
            return 
        self.items.pop()

    def isEmpty(self):
        return self.items == 0

    def getMultipleof(self, k):
        s = Stack()

        for x in self.items:
            if x % k == 0:
                s.push(x)
        
        return s

    def reverse(self):
        s = Stack()

        l = reversed(self.items)
        for x in l:
            s.push(x)

        return s
    
    def getAvg(self):
        if self.isEmpty():
            return 0
        
        return sum(self.items) / len(self.items)
    
    def min(self):
        if not self.items:
            return None
        return min(self.items)
    
    def deleteSecondItem(self):
        s = Stack()

        c = 0
        for x in self.items:
            if c != 1:
                s.push(x)
            c += 1
        
        self.items = s.items
    
    def display(self):
        print(self.items)

def isPalidrome(string):
    stack = Stack()

    for char in string:
        stack.push(char)

    for char in string:
        if char != stack.pop():
            return False
    return True
    
def isMatching(string):
    s = Stack()

    for x in string:
        if x in '[{(':
            s.push(x)
        elif x in ']})':
            p = s.pop()
            if (p == '(' and x != ')') or (p == '{' and x != '}') or (p == '[' and x != ']'):
                return False
            
    return s.is_empty()

def decodeMessage(string):
    s = Stack()

    result = ''
    for x in string:
        if x == '*':
            if not s.is_empty():
                result += s.pop()
        else:
            s.push(x)

    while not s.is_empty():
        result += s.pop()

    return result


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self): # o(n)
        if self.isEmpty():
            return 
        self.items.pop(0)

    def isEmpty(self):
        return self.items == 0
    
    def getMultipleof(self, s, n, m):
        s1 = Stack()
        s2 = Stack()
        for value in s.items:
            if value % n == 0:
                s1.push(value)
            if value % m == 0:
                s2.push(value)
        
        result_queue = Queue()
        for value in s1.items:
            result_queue.enqueue(value)
        for value in s2.items:
            result_queue.enqueue(value)
        
        return result_queue
    
    def secondMax(self):
        temp = self.items[::]
        l = max(temp)

        temp.remove(l)
        return max(temp)
    
    def display(self):
        return self.items
    
# Creating and populating the queue
# q = Queue()
# q.enqueue(5)
# q.enqueue(3)
# q.enqueue(9)
# q.enqueue(2)
# q.enqueue(8)

# # Display the initial queue
# print("Queue:", q.display())

# # Testing dequeue
# print("Dequeued element:", q.dequeue())
# print("Queue after dequeue:", q.display())

# # Testing getMultipleof with a stack
# s = Stack()
# s.push(3)
# s.push(6)
# s.push(9)
# s.push(12)
# print("Queue with multiples of 3 and 4:", q.getMultipleof(s, 3, 4).display())
# print("Second Maximum:", q.secondMax())
# print("Queue:", q.display())

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self):
        # return self.head == None
        return self.size == 0

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
        if not self.isEmpty():
            if self.size == 1:
                self.head = None
                self.tail = None
                self.size = 0
            else:
                self.head = self.head.next
                self.size -=  1
            return True
       
    def deleteTail(self):
        if not self.isEmpty():
            if self.size == 1:
                self.head = None
                self.tail = None
                self.size = 0
            else:
                temp = self.head

                while temp.next.next != None:
                    temp = temp.next
                
                temp.next = None
                self.tail = temp
                
                self.size -=  1
            return True
        
    def deleteElement(self, val):
        if self.isEmpty():
            return False

        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True
            
        currentNode = self.head
        prev = None

        while currentNode != None and currentNode.val != val:
            prev = currentNode
            currentNode = currentNode.next
                    
        if currentNode != None:
            prev.next = currentNode.next
            self.size -= 1
            return True

        return False
        

    def searchElement(self, val):
        if self.isEmpty():
            return -1

        currentNode = self.head
        index = 0
        while currentNode != None:
            if currentNode.val == val:
                return index
            currentNode = currentNode.next
            index += 1
        
        return -1

    def insertAt(self, position, val):
        if position < 0 or position >= self.size:
            return False
        
        if self.isEmpty():
            return False
        
        if position == 0:
            self.addToHead(val)
            return True
        
        if position == self.size-1:
            self.addToTail(val)
            return True
        
        index = 0
        currentNode = self.head

        while currentNode != None and index+1 != position:
            currentNode = currentNode.next
            index += 1
        
        if currentNode != None:
            n = Node(val, currentNode.next)
            currentNode.next = n
            self.size += 1
            return True
        else:
            return False
        

    def deleteAt(self, position):
        if self.isEmpty() or position < 0 or position >= self.size:
            return False
        
        if position == 0:
            self.deleteHead()
            return True
        
        if position == self.size-1:
            self.deleteTail()
            return True
        
        currentNode = self.head
        index = 0

        while currentNode != None and index + 1 != position:
            currentNode = currentNode.next
            index += 1
        
        if currentNode != None:
            currentNode.next = currentNode.next.next
            self.size -= 1

        
    def occurrenceNb(self, nb):
        count = 0

        c = self.head

        while c != None:
            if c.val == nb:
                count += 1
            c = c.next
        
        return count

    def oddNb(self):
        count = 0

        c = self.head

        while c != None:
            if c.val % 2 != 0:
                count += 1
            c = c.next
        
        return count

    def deleteEven(self):
        c = self.head
        deleted = False
        while c != None:
            if c.val % 2 == 0:
                self.deleteElement(c.val)
                deleted = True
            c = c.next
        
        return deleted

    def reverseList(self):
        currentNode = self.head
        prev = None

        while currentNode != None:
            nextNode = currentNode.next

            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode
        
        self.head = prev

    def oddEven(self):
        even = LinkedList()
        odd = LinkedList()

        currentNode = self.head
        
        while currentNode != None:
            if currentNode.val % 2 == 0:
                even.addToTail(currentNode.val)
            else:
                odd.addToTail(currentNode.val)

            currentNode = currentNode.next

        return [even, odd]
        
    def sortll(self):
        
        if self.isEmpty():
            return
        
        l = []
        currentNode = self.head
        
        while currentNode != None:
            l.append(currentNode.val)
            currentNode = currentNode.next

        l.sort()

        currentNode = self.head #none
        for x in l:
            currentNode.val = x
            currentNode = currentNode.next
        
    def mergeTwoLists(self, L1):
        if not self.head: #isempty
            self.head = L1.head
            return
        
        current = self.head
        while current.next != None:
            current = current.next

        current.next = L1.head
        
    def display(self):
        if not self.isEmpty():
            temp = self.head

            while temp != None:
                print(temp.val, ' -> ',end = " ")
                temp = temp.next
            print()
        else:
            print("EMpty linkedlist.")


l = LinkedList()
l.addToTail(2)
l.addToTail(3)
l.addToTail(2)
l.addToTail(1)
l.addToTail(4)
l.insertAt(2, 10)
# l.deleteTail()
# l.deleteElement(77)
# print(l.deleteAt(3))
# print(l.occurrenceNb(1))
# print(l.oddNb())
# print(l.deleteEven())
# l.reverseList()
# print(l.o())
l.display()
l.sortll()
l.display()

# l2 = LinkedList()
# l2.addToTail(44)
# l2.addToTail(11)
# l2.addToTail(66)

# l.display()
# l.mergeTwoLists(l2)
# l.display()
    

