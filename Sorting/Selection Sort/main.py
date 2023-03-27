def selection_sort(numbers):
    def swap(i, j):
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]]

    for i in range(0, len(numbers)):
        k = i

        for j in range(i+1, len(numbers)):
            if(numbers[j] < numbers[i]):
                k = j
        
        swap(i, k)

    return numbers

print(selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))