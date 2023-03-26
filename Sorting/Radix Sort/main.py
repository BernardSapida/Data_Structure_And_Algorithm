import itertools
import math

def digit_count(n):
    if n == 0:
        return 0
    return math.floor(math.log10(abs(n)))+1

def get_max_digit(numbers):
    max_digit = 0

    for n in numbers:
        digits = digit_count(n)

        if(digits > max_digit):
            max_digit = digits
    
    return max_digit

def get_digit(n, i):
    return math.floor(abs(n) / math.pow(10, i)) % 10

def radix_sort(numbers):
    max_digit_count = get_max_digit(numbers)

    for i in range(max_digit_count):
        digit_buckets = [[] for i in range(10)]

        for k in range(len(numbers)):
            digit = get_digit(numbers[k], i)
            digit_buckets[digit].append(numbers[k])

        numbers = list(itertools.chain(*digit_buckets))

    return numbers
        
print(radix_sort([9, 8, 7, 6]))

# Time Complexity: O(n+k)