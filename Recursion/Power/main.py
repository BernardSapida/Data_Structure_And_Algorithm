def power(n, p):
    if p == 0: return 1
    if p % 2 == 0:
        return power(n*n, p/2)
    elif p % 2 != 0:
        return n * power(n*n, (p-1)/2)

print(power(2, 60))