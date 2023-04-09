def traverse(arr):
    last = len(arr) # 3
    
    def helper(i, sum):
        # base case
        if i == last:
            return sum
        
        sum += arr[i]
        
        # Recursive call
        return helper(i+1, sum)

    return helper(0, 0)
    
print(traverse([1, 2, 3])) # 3
# return helper(0, 0) # sum = 6
# return helper(1, 1) # sum = 6
# return helper(2, 1) # sum = 6
# return helper(3, 1) # return sum = 6