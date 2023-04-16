def lengthOfLastWord(s):
    length = 0
    pos = len(s)-1
    
    # This while loop is used to skip any trailing spaces at the end of the input string `s`. It
    # starts at the end of the string and decrements the `pos` variable until it reaches a non-space
    # character. This ensures that the length of the last word is calculated correctly, without
    # including any trailing spaces.
    while s[pos] == " ":
        pos -= 1
    
   
   # This while loop is used to calculate the length of the last word in the input string `s`. It
   # starts at the position of the last non-space character (which was found in the previous while
   # loop that skipped any trailing spaces), and decrements the `pos` variable until it reaches the
   # beginning of the string or a space character. For each non-space character encountered, the
   # `length` variable is incremented. Once a space character is encountered or the beginning of the
   # string is reached, the loop stops and the final value of `length` is returned as the length of
   # the last word in the input string.
    while pos >= 0 and s[pos] != " ":
        length += 1
        pos -= 1
        
    return length