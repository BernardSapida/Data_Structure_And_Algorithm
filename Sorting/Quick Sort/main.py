def partition(array, low, high):
    def swap(arr, i, j):
        [arr[i], arr[j]] = [arr[j], arr[i]]

    pivot = array[high]
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    
    swap(array, i+1, high)
    return i + 1
 
def quick_sort(array, low, high):
    if low < high: 
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array
 
print(quick_sort([10, 16, 8, 12, 15, 6, 3, 9, 5], 0, 8))