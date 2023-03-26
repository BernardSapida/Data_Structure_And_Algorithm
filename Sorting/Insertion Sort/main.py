def insertion_sort(numbers):
    def swap(i, j):
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]]

    for i in range(1, len(numbers)):
        swapped = False

        for k in range(i-1, -1, -1):
            if numbers[i] < numbers[k]:
                swap(i, k)
                i -= 1
                swapped = True

            if not swapped:
                break
        
    return numbers

print(insertion_sort([1, 2, 3, 9, 8, 7, 6, 5, 4]))