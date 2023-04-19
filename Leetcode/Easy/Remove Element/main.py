# https://leetcode.com/problems/remove-element/

def removeElement(nums, val):
    count = 0
    
    # This code is iterating through the list `nums` and checking if each element is equal to the
    # value `val`. If an element is not equal to `val`, it is assigned to the `count` index of the
    # `nums` list and `count` is incremented. This effectively removes all occurrences of `val` from
    # the list and returns the new length of the list.
    for num in nums:
        if num != val:
            nums[count] = num
            count += 1
            
    return count