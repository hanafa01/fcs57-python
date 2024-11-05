
l = [1,2,3,4,5,6]

def binarySearch(list1, key): #O(logn)
    start = 0
    end = len(l)-1

    while start <= end:
        mid = (start + end) // 2
        if list1[mid] == key:
            return mid
        elif list1[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

def binarySearchRecursive(list1, key, start, end):
    if start <= end:
        mid = (start + end) // 2
        if list1[mid] == key:
            return mid
        elif list1[mid] < key:
            return binarySearchRecursive(list1, key, mid+1, end)
        else:
            return binarySearchRecursive(list1, key, start, mid-1) 
    else:
        return -1


print(binarySearchRecursive(l, 2, 0, len(l)-1))