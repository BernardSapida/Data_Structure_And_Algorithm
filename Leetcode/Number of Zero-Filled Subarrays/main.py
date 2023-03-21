def zeroFilledSubarray(nums):
    occurence = 0
    zeroes = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes += 1
            occurence += zeroes
        else:
            zeroes = 0
    return occurence

print(zeroFilledSubarray([1,3,0,0,2,0,0,4]))
print(zeroFilledSubarray([0,0,0,2,0,0]))
print(zeroFilledSubarray([2,10,2019]))