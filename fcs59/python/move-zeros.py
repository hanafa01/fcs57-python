def move_zeros(nums):
    l = []
    for x in nums:
        if x!=0:
            l.append(x)

    count_zeros = nums.count(0)
    
    return l + [0] * count_zeros

print(move_zeros([1, 2, 0, 5, 0, 11, 3, 0, 56]))