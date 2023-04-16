def isAnagram(s, t):
    occurence = {}
    
    # This code is creating a dictionary called `occurence` that will store the frequency of each
    # character in the string `s`. The `for` loop iterates through each character in `s`, and if the
    # character is already in the `occurence` dictionary, its frequency is incremented by 1. If the
    # character is not yet in the dictionary, it is added with a frequency of 1.
    for char in s:
        if char in occurence:
            occurence[char] += 1
        else:
            occurence[char] = 1
    
    # This code is iterating through each character in the string `t` and checking if it is present in
    # the `occurence` dictionary. If the character is present, its frequency is decremented by 1. If
    # the frequency becomes 0, the character is removed from the dictionary using the `del` keyword.
    # If the character is not present in the dictionary, it means that it is not an anagram of `s`, so
    # the function returns `False`. If all characters in `t` are present in `occurence` and their
    # frequencies match with those in `s`, the function returns `True`, indicating that `t` is an
    # anagram of `s`.
    for char in t:
        if char in occurence:
            if occurence[char] == 1:
                del occurence[char]
            else:
                occurence[char] -= 1
        else:
            return False
    
    # `is_empty_occurence = len(occurence) == 0` is checking if the dictionary `occurence` is empty or
    # not. If the length of `occurence` is equal to 0, it means that all characters in `s` have been
    # matched and removed by the second `for` loop, and therefore `t` is an anagram of `s`. In this
    # case, `is_empty_occurence` will be assigned the value `True`. If `occurence` is not empty, it
    # means that there are still unmatched characters in `s`, and therefore `t` is not an anagram of
    # `s`. In this case, `is_empty_occurence` will be assigned the value `False`. The variable
    # `is_empty_occurence` is then returned by the function to indicate whether `t` is an anagram of
    # `s` or not.
    is_empty_occurence = len(occurence) == 0
    
    return is_empty_occurence