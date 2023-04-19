# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    occurrence = {}
    
    # This code is checking if there are any duplicate elements in the given list `nums`. It
    # creates a dictionary `occurrence` to keep track of the occurrences of each element in the
    # list. It then iterates through the list using a for loop and checks if the current element
    # `nums[i]` is already present in the `occurrence` dictionary. If it is, then it means that
    # the element is a duplicate and the function returns `True`. If it is not present, then it
    # adds the element to the `occurrence` dictionary with a value of 1. If the loop completes
    # without finding any duplicates, then the function returns `False`.
    for i in range(len(nums)):
        if nums[i] in occurrence:
            return True
        else:
            occurrence[nums[i]] = 1
            
    return False