def get_median(B, A):
    total = len(B) + len(A)
    half = total//2

    if len(B) < len(A):
        B, A = A, B

    low, high = 0, len(A)-1

    while True:
        midA = low + (high - low) // 2 # A
        midB = half - midA - 2 # B

        leftA = A[midA] if midA >= 0 else float("-infinity")
        rightA = A[midA + 1] if midA + 1 < len(A) else float("infinity")
        leftB = B[midB] if midB >= 0 else float("-infinity")
        rightB = B[midB + 1] if midB + 1 < len(B) else float("infinity")

        if leftA <= rightB and leftB <= rightA:
            if total % 2 == 1:
                return min(rightA, rightB)
            else:
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
        elif leftA > rightB:
            high = midA - 1
        elif rightA < leftB:
            low = midB + 1

print(get_median([4, 9, 11, 11, 12, 15], [1, 1, 3, 5, 10]))