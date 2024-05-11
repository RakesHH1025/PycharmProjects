str='python narayana tech house'
str=str.split()
str1=' '
for i in str:
    str1=str1+i[0].upper()+i[1:].lower()
print(str1)