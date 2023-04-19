# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

def countGoodSubstrings(str):
    count=0
    
   # This code is counting the number of substrings of length 3 in the given string `str` that have
   # exactly 3 distinct characters.
    for i in range(len(str)-2):
        three_chars = str[i:(i+3)]
        
        if len(set(three_chars))==3:
            count+=1
            
    return count