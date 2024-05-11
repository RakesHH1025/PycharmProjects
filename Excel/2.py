from openpyxl import Workbook

# Create a new workbook
wb = Workbook()

# Select the active worksheet
ws = wb.active

# Data to write into the worksheet
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Write data into the worksheet
for row in data:
    ws.append(row)

# Save the workbook
wb.save("example.xlsx")
