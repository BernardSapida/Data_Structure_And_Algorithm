# https://leetcode.com/problems/valid-parentheses/

from collections import deque

def isValid(sts):
    stack = deque()

    for char in sts:
        if char == "(":
            stack.append(")")
        elif char == "[":
            stack.append("]")
        elif char == "{":
            stack.append("}")
        else:
            if stack.__len__() == 0 or char != stack.pop():
                return False
    
    return stack.__len__() == 0
        

print(isValid("(]"))
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("([]{})"))