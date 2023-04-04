n, lo, hi = map(int, input().split())
L = list(map(int, input().split()))

def binary_search(arr, target, is_lo):
    def helper(lo, hi, target):
        mid = int(lo + (hi - lo) / 2)
        pos = None

        if lo > hi:
            return -1
        elif arr[mid] == target:
            return mid
        elif target > arr[mid]:
            pos = helper(mid+1, hi, target)
        else:
            pos = helper(lo, mid-1, target)

        if pos == -1:
            return mid
        elif is_lo:
            if pos == len(L)-1:
                return pos
            elif arr[pos] >= target:
                return pos
        elif not is_lo:
            if pos == 0:
                return 0
            elif arr[pos] <= target:
                return pos
            
        return mid

    return helper(0, len(arr)-1, target)

def get_number_of_missing(L, lo, hi):
    lo_index = binary_search(L, lo, True)
    hi_index = binary_search(L, hi, False)
    range = get_range(lo, hi)

    if lo <= L[lo_index] and hi >= L[hi_index]:
        return range - (hi_index-lo_index+1)
    else:
        return range

def get_range(lo, hi):
    return hi - lo + 1

L.sort()

# print(get_number_of_missing(L, lo, hi))
# print(get_number_of_missing(L, -1, 3)) # 5
# print(get_number_of_missing([1, 2, 3, 4, 5, 6, 7], 3, 5)) # 0
# print(get_number_of_missing([1, 2, 4, 5, 6, 7], 3, 5)) # 1
# print(get_number_of_missing([1, 2, 3, 4, 6, 7], 3, 5)) # 1
# print(get_number_of_missing([1, 2, 4, 6, 7], 3, 5)) # 2
print(get_number_of_missing([1, 2, 4, 6, 7], -1, 0)) # 2
# print(get_number_of_missing([1, 2, 4, 6, 7], 20, 28)) # 9
# print(get_number_of_missing([15, 21, 4, 8, 9, 7, 11, 30, 1, 17], -1, 3)) # 5