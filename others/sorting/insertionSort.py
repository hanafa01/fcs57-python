
l = [10,2,-1,30,9,13]

for i in range(1, len(l)):
    key = l[i]
    j = i - 1
    while j >= 0 and l[j] > key:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = key

print(l)