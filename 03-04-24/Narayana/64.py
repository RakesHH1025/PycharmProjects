def print_pattern(rows):
    # Print the upper half of the pattern
    for i in range(1, rows + 1):
        print("   " * (rows - i) + "* " * i)

    # Print the lower half of the pattern
    for i in range(rows - 1, 0, -1):
        print("   " * (rows - i) + "* " * i)

print_pattern(5)  # You can adjust the argument to change the number of rows
