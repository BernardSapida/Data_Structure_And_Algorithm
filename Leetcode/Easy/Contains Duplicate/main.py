class Solution(object):
    def containsDuplicate(self, nums):
        occurrence = {}
        
        for i in range(len(nums)):
            if nums[i] in occurrence:
                return True
            else:
                occurrence[nums[i]] = 1
        return False