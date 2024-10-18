l = [1,3,56,234,789]
l.sort()
v = 4

def addElement(list1, value, start, end):
    if start >= end:
        list1.insert(start, value)
        return list1
    mid = (start+end)//2
    if list1[mid] > value:
        return addElement(list1, value, start, mid)
    elif list1[mid] < value:
        return addElement(list1, value, mid+1, end)
    else:
        list1.insert(mid+1, value)
        return list1
    
print(addElement(l, v, 0, len(l)))


#O(n)
# b = False
# for i in range(0, len(l)):
#     if v < l[i]:
#         l.insert(i, v)
#         b = True
#         break

# if b == False:
#     l.append(v)

# print(l)