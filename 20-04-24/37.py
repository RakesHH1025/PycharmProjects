str1 = "Emma25 is Data scientist50 and AI Expert"
str=str1.split(" ")
for word in str:
    if any(char.isalpha() for char in word) and any (char.isdigit() for char in word):
        print(word)

