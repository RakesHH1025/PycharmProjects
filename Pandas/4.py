import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')

# Write to CSV
df.to_csv('new_data.csv', index=False)

# Display basic information
print(df.info())

# Display first few rows
print(df.head())

# Select specific columns
print(df['column_name'])

# Filter rows
print(df[df['column_name'] > 10])



