

def longest_subarray(array):
    # Initialize with sum 0 at index -1
    count_map = {0: -1}  
    # Initialize both at starting 0
    max_length, count = 0, 0
    

    for index, value in enumerate(array):
        count += 1 if value == 1 else-1  # Increment if 1, otherwise decrement by 0
        
        if count in count_map:
            #calculate the length of the longest subarray
            max_length = max(max_length, index - count_map[count])
        else:
            # Store this count
            count_map[count] = index 

    return max_length


array = [0, 1, 0, 1, 1, 0, 0]
print(longest_subarray(array))