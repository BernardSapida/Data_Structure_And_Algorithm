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

def get_digit(n, i, d = 1):
    if d == 1:
        return math.floor(abs(n) / math.pow(10, i)) % 10
    else:
        return math.floor(abs(n) / math.pow(10, i)) % pow(10, d)

def radix_sort(numbers, number_of_digits = 1):
    max_digit_count = get_max_digit(numbers)

    for i in range(0, max_digit_count, number_of_digits):
        digit_buckets = [[] for _ in range(pow(10, number_of_digits))]

        for k in range(len(numbers)):
            digit = get_digit(numbers[k], i, number_of_digits)
            digit_buckets[digit].append(numbers[k])

        numbers = list(itertools.chain(*digit_buckets))

    return numbers
        
print(radix_sort([121, 4010, 1009, 2100], 1))

# Time Complexity: O(n+k)