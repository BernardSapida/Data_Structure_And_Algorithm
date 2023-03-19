A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 9

def target_exist(arr, target, i = 0):
    # base case
    if i == len(arr): 
        return -1

    # loop to current arr
    found = find_target(arr[i], target)

    # check if target found
    if found:
        return True
    
    # traverse to next array
    return target_exist(arr, target, i+1)

def find_target(arr, target, i=0):
    # when index is equal to arr length it means target is not found
    if i == len(arr):
        return False
    
    # when current value is equal to target. Return True since it is found
    if arr[i] == target:
        return True
    
    # traverse to next value
    return find_target(arr, target, i+1)

for i in range(1, 10):
    # let i be the target value
    # it should produce 9 True results since 1-9 is found in array 
    print(target_exist(A, i), i)

# Problem: Implement a recursive function that returns true if an element 𝑥 is in a 2-dimensional array 𝐴
# otherwise it prints false. 