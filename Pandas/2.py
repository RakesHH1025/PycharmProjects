# Reading and Writing Data:
import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')

# Write to CSV
df.to_csv('new_data.csv', index=False)
