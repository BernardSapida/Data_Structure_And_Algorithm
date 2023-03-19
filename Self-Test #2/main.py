A = [1, 2, 3, 4, 5]
d = 5

def print_numbers_divisible_by_d(arr, d, i = 0):
    # Base case
    if i == len(arr):
        return
    
    # When the remainder of current value divide d is 0
    # print current value
    if arr[i] % d == 0:
        print(arr[i])

    # traverse to next value
    print_numbers_divisible_by_d(arr, d, i+1)

print_numbers_divisible_by_d(A, d)

# Problem: Create a recursive function that takes as input an array 𝐴 of positive integers and a number 
# 𝑑 then prints all numbers in 𝑎 divisible by 𝑑, one line at a time. 