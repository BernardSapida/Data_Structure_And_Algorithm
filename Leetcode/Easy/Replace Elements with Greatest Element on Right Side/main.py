def replaceElements(arr):
    low = 0
    
    # This code block is checking if the input array `arr` has only one element. If it does, it
    # replaces the element with the value `-1` and returns the modified array. This is done because
    # the problem statement specifies that if the input array has only one element, the output array
    # should be `-1`.
    if len(arr) == 1:
        arr[0] = -1
        return arr
    
    # a while loop to iterate through the array, starting at the first element and ending at the
    # second-to-last element.
    while low != len(arr)-1:
        max = float("-infinity")
        steps = 0
        
        # This code is finding the maximum element to the right of the current element (at index
        # `low`) in the array `arr`. It does this by iterating through the array starting at the index
        # `low+1` and ending at the last index `len(arr)-1`. If it finds an element greater than the
        # current maximum (`max`), it updates `max` to be that element and calculates the number of
        # steps needed to reach that element (`i - low`). The number of steps is stored in the
        # variable `steps`.
        for i in range(low+1, len(arr)):
            if arr[i] > max:
                max = arr[i]
                steps = i - low
        
        # This code is replacing the elements in the array `arr` starting from the index `low` and
        # ending at the index `low + steps - 1` with the maximum element found in the previous loop.
        # This ensures that all elements to the right of the current element (at index `low`) are
        # replaced with the maximum element.
        for i in range(low, low + steps):
            arr[i] = max
        
        # `low += steps` is updating the value of `low` to be the index of the next element that needs
        # to be replaced with the maximum element. It adds the number of steps taken in the previous
        # loop to `low` so that the next iteration of the while loop starts at the correct index.
        low += steps
                
    # `arr[len(arr)-1] = -1` is replacing the last element of the input array `arr` with the value
    # `-1`. This is done because the last element of the output array should always be `-1`, as per
    # the problem statement.
    arr[len(arr)-1] = -1
    
    return arr

print(replaceElements([17,18,5,4,6,1]))
print(replaceElements([1,2,3,4,5,6,10]))
            
"""
      0  1 2 3 4 5
    [17,18,5,4,6,1]
        l      i
        
    steps = 4 - 1 - 1 = 2
"""