for i in range(4):
    spaces = " " * i  # Create spaces based on the current row number
    stars = "*" * (4 - i)  # Create asterisks based on the remaining space in the row
    print(spaces + stars)  # Concatenate and print spaces and asterisks for each row
