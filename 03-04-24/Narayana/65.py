def print_pattern(rows):
    for i in range(1, rows + 1):
        print("* " * i)
    print()
    for i in range(rows, 0, -1):
        print("* " * i)

print_pattern(6)  # You can adjust the argument to change the number of rows
