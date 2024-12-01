
class ArrayInt:

    def __init__(self, size):
        self.items = []
        self.size = size
        self.currentNb = 0  #length

    def isEmpty(self):
        return self.currentNb == 0

    def isFull(self):
        return self.currentNb == self.size

    def insertElementAtFront(self, val):
        if not self.isFull():
            self.items.append(val)
            self.currentNb += 1
            return True
        return False

    def insertElementAtBack(self, val):
        if not self.isFull():
            self.items.insert(0, val)
            self.currentNb += 1
            return True
        return False
    
    def insertElementAtMiddle(self, val):
        if not self.isFull():
            mid = self.currentNb // 2
            self.items.insert(mid, val)
            self.currentNb += 1
            return True
        return False
    
    def searchValue(self, val):
        index = -1

        if not self.isEmpty():
            for i in range(self.currentNb):
                if self.items[i] == val:
                    index = i
                    break
        
        return index
    
    def deleteValue(self, val):
        if not self.isEmpty():
            for i in range(self.currentNb):
                if self.items[i] == val:
                    self.items.pop(i)
                    self.currentNb -= 1
                    return True
        
        return False
    
    def avgOfItems(self):
        if not self.isEmpty():
            sum = 0
            for i in self.items:
                sum += i
        
            return sum/self.currentNb
        return 0
    
    def occurenceNb(self, val):
        if not self.isEmpty():
            count = 0
            for i in self.items:
                if i == val:
                    count += 1
            return count
        return 0
    
    def palindrome(self):
        low = 0
        high = self.currentNb - 1

        while low < high:
            if self.items[low] != self.items[high]:
                return False
            low+=1
            high-=1

        return True
    
    def deleteEven(self):
        if not self.isEmpty():
            for i in self.items:
                if i % 2 == 0:
                    self.deleteValue(i)
    
    def countOddItems(self):
        return self.currentNb - self.countEvenItems()
    
    def countEvenItems(self):
        count = 0
        if not self.isEmpty():
            for i in self.items:
                if i % 2 == 0:
                   count += 1
        
        return count
    
    def evenOrOdd(self):
        return (self.countEvenItems() > self.countOddItems())
   
    # def sortArrayDesc(self):
    #     if self.isEmpty():
    #         print('No items.')
    #     else:
    #         self.items = self.items.sort(reverse=True)
    #         for i in self.items:
    #             print(i, end=" ")

    def printItems(self):
        if self.isEmpty():
            print('No items.')
        else:
            for i in self.items:
                print(i, end=" ")


a = ArrayInt(8)
a.insertElementAtFront(4)
a.insertElementAtFront(5)
a.insertElementAtBack(3)
a.insertElementAtBack(2)
a.insertElementAtBack(1)
a.insertElementAtMiddle(10)
print(a.searchValue(2))
a.printItems()
print(a.deleteValue(10))
print(a.avgOfItems())
print(a.occurenceNb(1))
a.printItems()
print(a.palindrome())
# a.deleteEven()
a.printItems()
print()
print(a.countOddItems())
print(a.countEvenItems())
print(a.evenOrOdd())
print(a.evenOrOdd())
print()

a.sortArrayDesc()

a.printItems()
