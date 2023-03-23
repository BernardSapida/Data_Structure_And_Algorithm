def TOH(n, source, destination, extra):
    if n > 0:
        TOH(n-1, source, extra, destination)
        print(f"Move {source} to {destination}")
        TOH(n-1, extra, destination, source)

TOH(3, 1, 3, 2)