def bubble_sort(numbers):
    def swap(i, j):
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]]

    last_index_sorted = len(numbers)-1

    while True:
        swapped = False

        for i in range(last_index_sorted):
            if numbers[i] > numbers[i+1]:
                swap(i, i+1)
                swapped = True
        
        if not swapped:
            return numbers
        
        last_index_sorted -= 1

print(bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
