for i in range(1, 5):  # Outer loop for rows from 1 to 4
    spaces = " " * (4 - i)  # Calculate the number of spaces needed
    stars = "*" * i  # Calculate the number of asterisks needed
    print(spaces + stars)  # Print spaces followed by asterisks for each row
