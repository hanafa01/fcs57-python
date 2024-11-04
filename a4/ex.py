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
            
    def printll(self):
        temp = self.head
        while temp != None:
            print(temp.val, ' -> ', end = " ")
            temp = temp.next

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

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



# string = input("Enter a string to check if it is palindrome: ")
# print(isPalidrome(string))

# ex = input("Enter the expression to determine if a given expression is balanced: ")
# print(isMatching(ex))

# msg = input("Enter message to decode: ")
# print(decodeMessage(msg))

# print(isPalidrome('hellolleh'))
# print(isMatching('(1+2)-3*[41+6]'))
# print(decodeMessage('SIVLE ****** DAED TNSI ***'))


ll = LinkedList()

ll.addToHead(0)
ll.addToHead(11)
ll.addToHead(76)
ll.addToHead(56)
ll.addToHead(12)

print("Default LinkedList:")
ll.printll()
print()
print("Enter an index to delete:")
index = input()
if not index.isdigit():
    print("number should be integer")
else:
    index = int(index)
    print("LinkedList after removing:")
    ll.remove_at(index)    
    ll.printll()
    print()