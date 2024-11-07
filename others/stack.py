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