# https://leetcode.com/problems/isomorphic-strings/

def isIsomorphic(s, t):
    occurrence = {}
    
    # This code is iterating through each character in the strings `s` and `t` using a for loop. For
    # each character, it checks if the character from `s` is already in the `occurrence` dictionary.
    # If it is not, it adds the character from `s` as a key and the corresponding character from `t`
    # as its value in the `occurrence` dictionary. If the character from `s` is already in the
    # `occurrence` dictionary, it checks if the corresponding value is equal to the character from
    # `t`. If it is not, it means that the same character in `s` is being mapped to different
    # characters in `t`, so the function returns `False`. If the loop completes without returning
    # `False`, it means that the strings are isomorphic and the function returns `True`.
    for i in range(len(s)):
        charS = s[i]
        charT = t[i]
        
        if charS in occurrence:
            if occurrence[charS] != charT:
                return False
            continue
        
        if (charT in occurrence and occurrence[charT] == charT) or (charS in occurrence and occurrence[charS] == charS):
            return False
        
        occurrence[charS] = charT
            
    return True