# https://leetcode.com/problems/generate-parentheses/

def get_pairs(n):
    result = []
    stack = []

    def backtrack(open, close):
        # This code block checks if the number of opening parentheses and closing parentheses are
        # equal to the given value of `n`. If they are equal, it means that a valid pair of
        # parentheses has been formed and it is added to the `result` list by joining the elements of
        # the `stack` list. The `return` statement is used to exit the function and continue with the
        # next iteration of the recursion.
        if open == close == n:
            result.append("".join(stack))
            return

        # This code block is checking if the number of opening parentheses is less than the given
        # value of `n`. If it is less, it means that another opening parenthesis can be added to the
        # `stack` list. So, an opening parenthesis is appended to the `stack` list, and the
        # `backtrack` function is called recursively with `open+1` and `close` as arguments. This will
        # add another opening parenthesis to the `stack` list and move to the next level of recursion.
        # After the recursion is complete, the last element of the `stack` list (which is the opening
        # parenthesis) is removed using `stack.pop()`.
        if open < n:
            stack.append("(")
            backtrack(open+1, close)
            stack.pop()

        # This code block is checking if the number of closing parentheses is less than the number of
        # opening parentheses. If it is less, it means that another closing parenthesis can be added
        # to the `stack` list. So, a closing parenthesis is appended to the `stack` list, and the
        # `backtrack` function is called recursively with `open` and `close+1` as arguments. This will
        # add another closing parenthesis to the `stack` list and move to the next level of recursion.
        # After the recursion is complete, the last element of the `stack` list (which is the closing
        # parenthesis) is removed using `stack.pop()`. This ensures that the `stack` list only
        # contains valid pairs of parentheses.
        if close < open:
            stack.append(")")
            backtrack(open, close+1)
            stack.pop()

    backtrack(0, 0)

    return result