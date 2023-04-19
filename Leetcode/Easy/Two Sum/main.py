# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    hash = {}
    
    for i in range(len(nums)):
        # `num = nums[i]` is assigning the value of the current element in the `nums` list to the
        # variable `num`.
        num = nums[i]
        
        # `difference = target - num` is calculating the difference between the target value and the
        # current element in the `nums` list. This difference represents the value that needs to be
        # found in the list in order to satisfy the two-sum problem.
        difference = target - num
        
        # This code is checking if the `difference` variable (which represents the value that needs to
        # be found in the list in order to satisfy the two-sum problem) is already in the `hash`
        # dictionary.
        if difference in hash:
            # `return [hash[difference], i]` is returning a list containing the indices of the two
            # numbers in the input `nums` list that add up to the `target` value. `hash[difference]`
            # retrieves the index of the first number needed to reach the target value, and `i` is the
            # index of the second number needed to reach the target value.
            return [hash[difference], i]
        else:
            # `hash[num] = i` is adding a key-value pair to the `hash` dictionary, where the key is
            # the current element `num` in the `nums` list and the value is the index `i` of that
            # element in the list. This is done so that later on, when iterating through the list, we
            # can quickly check if the difference between the target value and the current element has
            # already been encountered before. If it has, we can immediately return the indices of the
            # two numbers that add up to the target value.
            hash[num] = i