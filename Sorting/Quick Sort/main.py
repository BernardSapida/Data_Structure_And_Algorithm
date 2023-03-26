def partition(array, low, high):
    def swap(array, i, j):
        [array[i], array[j]] = [array[j], array[i]]

    pivot = array[low]
    pivot_index = low

    for i in range(low+1, high):
        current_value = array[i]
        
        if pivot >= current_value:
            pivot_index += 1
            swap(array, pivot_index, i)
    
    swap(array, low, pivot_index)

    return pivot_index
 
def quick_sort(array, low, high):
    if low < high: 
        mid = partition(array, low, high)
        quick_sort(array, low, mid)
        quick_sort(array, mid + 1, high)

    return array

print(quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9))