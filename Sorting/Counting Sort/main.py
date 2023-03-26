def counting_sort(arr, min, max):
    j = 0;
    supplementary = [0]*(max+1);

    for i in range(0, len(arr)):
        supplementary[arr[i]] += 1

    for i in range(min, max+1):
        while supplementary[i] > 0:
            arr[j] = i
            j+=1
            supplementary[i] -= 1

    return arr
    
print(counting_sort([2, 3, 8, 7, 100, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2], 1, 100))
