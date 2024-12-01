def special_rearrangement(nums):
    l_even = []
    l_odd = []

    for x in nums:
        if x % 2 == 0:
            l_even.append(x)
        else:
            l_odd.append(x)

    return l_even+l_odd

print(special_rearrangement([1,2,4,6,2,1,3,7,9,10]))

