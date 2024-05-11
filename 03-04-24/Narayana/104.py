def number_pattern(n):
    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i) + (str(i) + " ") * i)
    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + (str(i) + " ") * i)

number_pattern(5)
