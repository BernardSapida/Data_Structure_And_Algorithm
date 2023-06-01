# n = input()
# L = list(map(int, input().split()))

def displayLineOfSight(L):
    highest_value = L[0]
    highest_value_index = 0
    count = 1
    output = [0]*len(L)

    for i in range(len(L)-1, 0, -1):
        output[i] = 0 if L[i] > L[i-1] else 1

    output[1] = 1
    for i in range(1, len(output)-1):
        count += 1

        if output[i+1] == 0:
            value = output[i] + output[i+1] + 1

            if count >= value:
                highest_count = output[highest_value_index]

                if L[i] > highest_value:
                    output[i+1] = count + highest_count
                else:
                    output[i+1] = count
                count = 0
            else:
                output[i+1] = value

            highest_value = L[i+1]
            highest_value_index = i+1

    # print(L)
    # print(output)
    # print()

    return output


# displayLineOfSight([3, 2, 1])
# displayLineOfSight([1, 2, 3])
# displayLineOfSight([5, 1, 2, 1, 3])
# displayLineOfSight([10, 3, 2, 10, 2, 1, 7])
# displayLineOfSight([192, 163, 185, 165, 165, 170, 180])
displayLineOfSight([10, 3, 2, 8, 2, 1, 7])
