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