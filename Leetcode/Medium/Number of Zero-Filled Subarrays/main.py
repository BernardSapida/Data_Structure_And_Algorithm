# https://leetcode.com/problems/number-of-zero-filled-subarrays/

def zeroFilledSubarray(nums):
    occurence = 0
    zeroes = 0
    
    # This code is iterating through the input list `nums` using a for loop. For each element in the
    # list, if the element is equal to 0, the variable `zeroes` is incremented by 1 and the value of
    # `occurence` is incremented by the current value of `zeroes`. This means that for each
    # consecutive zero in the list, the value of `occurence` will increase by the number of zeroes
    # seen so far. If the element is not equal to 0, the value of `zeroes` is reset to 0. The function
    # returns the final value of `occurence`.
    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes += 1
            occurence += zeroes
        else:
            zeroes = 0
            
    return occurence