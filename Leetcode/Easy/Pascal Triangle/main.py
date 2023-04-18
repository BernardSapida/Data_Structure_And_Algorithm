def generate(numRows):
    rows = []
    
    # This code block is checking if the input `numRows` is greater than or equal to 1. If it is, then
    # it appends a list containing the value 1 to the `rows` list. This is the first row of Pascal's
    # triangle, which always starts with a single 1.
    if numRows >= 1:
        rows.append([1])
        
    # This code block is checking if the input `numRows` is greater than or equal to 2. If it is, then
    # it appends a list containing two 1's to the `rows` list. This is the second row of Pascal's
    # triangle, which always starts with two 1's.
    if numRows >= 2:
        rows.append([1,1])
        
    # This code block is checking if the input `numRows` is less than or equal to 2. If it is, then it
    # immediately returns the `rows` list that was previously populated with the first two rows of
    # Pascal's triangle. This is because Pascal's triangle always starts with these two rows, and
    # there are no additional rows to generate if `numRows` is less than or equal to 2.
    if numRows <= 2:
        return rows
    
    # This code block is generating the remaining rows of Pascal's triangle. It starts at the third
    # row (index 2) and iterates up to the input `numRows`. For each row, it first retrieves the
    # previous row from the `rows` list using `row = rows[i-1]`. It then generates the current row by
    # adding a 1 to the beginning and end of the previous row, and computing the sum of adjacent
    # elements in the previous row using a list comprehension. The resulting row is then appended to
    # the `rows` list using `rows.append()`. Finally, the function returns the complete `rows` list
    # containing all the rows of Pascal's triangle up to the input `numRows`.
    for i in range(2, numRows):
        row = rows[i-1]
        rows.append([1] + [row[k] + row[k+1] for k in range(len(row)-1)] + [1])
        
    return rows
    
print(generate(10))