def isValid(str):
    arr = []

    def helper(arr, i):
        if i == len(str):
            return len(arr) == 0
        
        char = str[i]

        if char == "(":
            arr.append(")")
        elif char == "[":
            arr.append("]")
        elif char == "{":
            arr.append("}")
        else:
            if len(arr) == 0 or char != arr.pop():
                return False
        
        return helper(arr, i+1)
    
    return helper(arr, 0)
        
# print(isValid("(]"))
# print(isValid("()"))
# print(isValid("()[]{}"))
# print(isValid("([]{})"))
# print(isValid("((())"))
# print(isValid("[){]"))
# print(isValid("[({})]"))