class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0


#parentheses
def validParentheses(str):
    stack = Stack()

    for x in str:
        if x in '[({':
            stack.push(x)
        elif x in '])}':
            p = stack.pop()
            if (p == '(' and x != ')') or (p == '{' and x != '}') or (p == '[' and x != ']'):
                break

    return len(stack.items) == 0

# print(validParentheses("[()]{}{[()()]()}"))

#reverse
def reverse(str):
    stack = Stack()

    for x in str:
        stack.push(x)

    res = ''

    for x in str:
        res += stack.pop()
    
    return res

print(reverse('Hello World'))