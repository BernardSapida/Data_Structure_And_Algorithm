from collections import deque

def isValid(str):
    stack = deque()

    def helper(stack, i):
        if i == len(str):
            return stack.__len__() == 0
        
        char = str[i]

        if char == "(":
            stack.append(")")
        elif char == "[":
            stack.append("]")
        elif char == "{":
            stack.append("}")
        else:
            if stack.__len__() == 0 or char != stack.pop():
                return False
        
        return helper(stack, i+1)
    
    return helper(stack, 0)
        
print(isValid("(]"))
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("([]{})"))
print(isValid("((())"))
print(isValid("[){]"))
print(isValid("[({})]"))