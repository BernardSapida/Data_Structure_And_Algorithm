def longestCommonPrefix(strs):
    n = len(strs)
    min = len(strs[0])  
    
    for i in range(1,n):
        if (len(strs[i])< min):
            min = len(strs[i])
            
    prefix = ""

    for i in range(min):
        current = strs[0][i]    
        
        for j in range(1,n):
            if (strs[j][i] != current):
                return prefix
            
        prefix += current    
        
    return prefix