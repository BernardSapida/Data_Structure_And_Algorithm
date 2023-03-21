from collections import deque

class Solution:
    def isValid(self, sts):
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
        
solution = Solution()

print(solution.isValid("(]"))
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("([]{})"))