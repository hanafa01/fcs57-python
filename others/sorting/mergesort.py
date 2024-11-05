l = [10,2,-1,30,9,13]

#O(nlogn)

def mergeSort(list1, start, end): 
    if start == end:
        return 
    mid = (start + end) // 2

    mergeSort(list1, start, mid)
    mergeSort(list1, mid+1, end)

    merge(list1, start, end)
    return list1

def merge(l, start, end):
    mid = (start + end) // 2
    i = start
    j = mid+1
    temp = []
    while i<= mid and j <= end:
        if l[i] < l[j]:
            temp.append(l[i])
            i += 1
        else:
            temp.append(l[j])
            j += 1

    while i<= mid:
        temp.append(l[i])
        i += 1

    while j <= end:
        temp.append(l[j])
        j += 1

    l[start:end+1] = temp


print(mergeSort(l, 0, len(l) - 1))