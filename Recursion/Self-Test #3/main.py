A = [1, 2, 3, 4, 5]
x = 3

def find(arr, target, i = 0):
    # Base case
    if i == len(arr):
        return -1

    # Print index when current value is equal to target
    if arr[i] == target:
        return i
    
    # traverse to next value
    return find(arr, target, i+1)

print(find(A, x))

# Problem: Create a recursive function that returns the index of element 𝑥 in the array 𝐴 if 𝑥 is in the array, 
# otherwise it returns -1. Hint: If 𝑥 is in the array then it is either the first element or some other 
# element after the first element. 