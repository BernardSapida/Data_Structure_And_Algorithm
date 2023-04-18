def longestCommonPrefix(strs):
    n = len(strs)
    min = len(strs[0])  
    
    # This code is finding the length of the shortest string in the given list of strings `strs`. It
    # initializes the variable `min` with the length of the first string in the list and then iterates
    # over the remaining strings in the list using a `for` loop. For each string, it checks if its
    # length is less than the current value of `min`. If it is, then it updates the value of `min` to
    # be the length of that string. At the end of the loop, `min` will contain the length of the
    # shortest string in the list.
    for i in range(1,n):
        if (len(strs[i])< min):
            min = len(strs[i])
            
    prefix = ""

    # This code is finding the longest common prefix among a list of strings `strs`. It first finds
    # the length of the shortest string in the list using the `for` loop that iterates over the
    # strings in the list and updates the value of `min` to be the length of the shortest string.
    for i in range(min):
        current = strs[0][i]    
        
        for j in range(1,n):
            if (strs[j][i] != current):
                return prefix
            
        prefix += current    
        
    return prefix