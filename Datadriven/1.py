import pandas as pd

# Load the Excel file
excel_file = 'D:\Excceldata\data.xlsx'  # Replace with your file path
df = pd.read_excel(excel_file)

# Display the content of the DataFrame
print(df)
