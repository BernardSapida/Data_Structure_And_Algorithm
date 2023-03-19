def get_pairs(n):
    result = []
    stack = []

    def backtrack(open, close):
        if open == close == n:
            # append new complete pair parentheses
            result.append("".join(stack))
            return

        if open < n:
            stack.append("(")
            backtrack(open+1, close)
            stack.pop()

        if close < open:
            stack.append(")")
            backtrack(open, close+1)
            stack.pop()

    backtrack(0, 0)

    return result
    

print(get_pairs(2))

"""
    n = 2
    open = 2
    close = 2

    result = (()), ()()

    variables:
        n = number of pair open & close parentheses
        open = open parentheses
        close = close parentheses

    conditions:
        • when open and close and n are equal then we generate new valid pairs
        • generate ( if open < n
        • generate ) if close < open
"""