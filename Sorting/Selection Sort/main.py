def selection_sort(numbers):
    def swap(i, j):
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]]

    for i in range(0, len(numbers)):
        low_index = -1

        for k in range(i+1, len(numbers)):
            if(numbers[k] < numbers[i]):
                low_index = k
        
        if low_index == -1:
            return numbers
        else:
            swap(i, low_index)

print(selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))