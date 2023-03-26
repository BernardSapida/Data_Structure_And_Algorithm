from math import floor

def merge(list1, list2):
    sorted_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i+=1
        else:
            sorted_list.append(list2[j])
            j+=1

    while i < len(list1):
        sorted_list.append(list1[i])
        i+=1

    while j < len(list2):
        sorted_list.append(list2[j])
        j+=1

    return sorted_list

def merge_sort(numbers_list):
    if len(numbers_list) <= 1:
        return numbers_list
    
    mid = floor(len(numbers_list) / 2)
    left = merge_sort(numbers_list[:mid])
    right = merge_sort(numbers_list[mid:])

    return merge(left, right)

print(merge_sort([9, 8, 7, 6, 5]))