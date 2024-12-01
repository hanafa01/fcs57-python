
def first_missing_positive(l1):
    
    missing = 1 

    for i in range(1, len(l1)+1):
        if i not in l1:
            break
        
        missing +=1

    return missing


print(first_missing_positive([1,2,0]))