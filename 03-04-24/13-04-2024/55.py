str1 = "Emma25 is Data scientist50 and AI Expert"
res = []
temp = str1.split()
for i in temp:
    if any (char.isalpha for char in i) and any(char.isdigit() for i)