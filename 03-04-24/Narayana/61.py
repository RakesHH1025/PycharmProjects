for i in range(5):  # Outer loop for rows from 0 to 4
    row = ""  # Initialize an empty string for each row
    for j in range(1, 6):  # Inner loop for numbers from 1 to 5
        row += str(j)  # Append the current number to the row string
    print(row)  # Print the row
