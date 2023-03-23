def TOH(n, source, C, B):
    if n > 0:
        TOH(n-1, source, B, C)
        print(f"Move {source} to {C}")
        TOH(n-1, B, C, source)

TOH(3, 1, 3, 2)