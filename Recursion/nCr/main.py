# Combination
def combination(n, r):
    if r == 0 or n == r:
        return 1
    
    # Optimized by using pascal triangle
    return combination(n-1, r-1) + combination(n-1, r);

print(combination(4, 2))