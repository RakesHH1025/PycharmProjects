def number_pattern(n):
    # Upper triangle
    for i in range(n, 0, -1):
        print(" " * (n - i) + (str(n - i + 1) + " ") * i)
    # Lower triangle
    for i in range(2, n + 1):
        print(" " * (n - i) + (str(n - i + 1) + " ") * i)
    # Lower half of diamond
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + (str(i) + " ") * i)
    # Upper half of diamond
    for i in range(2, n + 1):
        print(" " * (n - i) + (str(i) + " ") * i)

number_pattern(5)
