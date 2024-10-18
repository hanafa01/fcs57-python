l = [-1, 20, 34, 56, 89, 100]

l.sort()


def binarySearch(l1, k, start, end):
      while start <= end: 
        mid = (start + end) // 2
        if l1[mid] == k:
            return True
        elif l1[mid] < k:
          return binarySearch(l1, k, mid+1, end)
        else:  
          return binarySearch(l1, k, start, mid-1)

      return False



print(binarySearch(l, 100, 0, len(l)-1))





