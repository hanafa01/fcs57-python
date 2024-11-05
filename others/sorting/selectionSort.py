l = [10,2,-1,30,9,13]


#o(n)
for i in range(0, len(l)):
    minIndex = i
    for j in range(i, len(l)):
        if l[j] < l[minIndex]:
            minIndex = j
    
    # temp = l[minIndex]
    # l[minIndex] = l[i]
    # l[i] = temp
    #or
    # l[minIndex],l[i] = l[i],l[minIndex]

print(l)
