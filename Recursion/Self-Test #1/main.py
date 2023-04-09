numbers = [1, 32, 13, 4, 25]

def computeMaximum(arr):
    return getMaximum(arr, 0, arr[0])

# Helper function to find max value
def getMaximum(arr, i, maxValue):
    # Base case
    if i == len(arr):
        return maxValue
    
    # Compare current value to max value
    # update current maxValue
    # traverse to next value
    return getMaximum(arr, i+1, max(arr[i], maxValue))

print(computeMaximum(numbers))

# Problem: Create a tail recursive function to compute the maximum value of an array. 