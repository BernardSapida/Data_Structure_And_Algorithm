def lengthOfLastWord(s):
    length = 0
    char_found = False
    
    # This code is iterating through the string `s` backwards, starting from the last character. It
    # checks if the current character is a space and if `char_found` is False, it continues to the
    # next character. If the current character is a space and `char_found` is True, it breaks out of
    # the loop. If the current character is not a space, it sets `char_found` to True and increments
    # the `length` variable. The loop continues until a space is found after a non-space character or
    # until the beginning of the string is reached. The function returns the length of the last word
    # in the string.
    for i in range(len(s)-1, -1, -1):
        if s[i] == " " and not char_found:
            continue
        elif s[i] == " " and char_found:
            break
        else:
            char_found = True
            
        length += 1
        
    # `return length` is returning the value of the `length` variable, which represents the length of
    # the last word in the input string `s`. This value is returned as the output of the
    # `lengthOfLastWord` function.
    return length