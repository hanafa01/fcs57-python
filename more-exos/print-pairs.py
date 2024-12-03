
def print_pairs(letters):
    
    if len(letters) <= 0:
        return 
    
    for i in range(1, len(letters)):
        print(letters[0] + letters[i])

    print_pairs(letters[1:])


print_pairs('ABCD')