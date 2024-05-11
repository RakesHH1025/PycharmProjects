str1 = "P@#yn26at^&i5ve"
chars=0
special=0
digits=0

for i in str1:
    if i.isalpha():
        chars=chars+1
    elif i.isdigit():
        digits=digits+1
    else:
        special=special+1
print(chars)
print(digits)
print(special)