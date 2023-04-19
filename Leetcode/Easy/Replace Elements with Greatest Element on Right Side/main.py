# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

def replaceElements(arr):
    max_value = -1
    
    
   # This code is iterating through the input array `arr` in reverse order, starting from the last
   # element and going backwards to the first element. For each element, it replaces the element with
   # the maximum element to its right (which is stored in the variable `max_value`). It also updates
   # `max_value` to be the maximum value between the current element and the previous `max_value`. The end
   # result is an array where each element is replaced with the maximum element to its right.
    for i in range(len(arr)-1,-1,-1):
        temp = arr[i]
        arr[i] = max_value
        max_value = max(max_value, temp)
        
    return arr

print(replaceElements([17,18,5,4,6,1]))
print(replaceElements([1,2,3,4,5,6,10]))
            
"""
      0  1 2 3 4 5
    [17,18,5,4,6,1]
        l      i
        
    steps = 4 - 1 - 1 = 2
"""