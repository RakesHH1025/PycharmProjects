str1 = 'I am 25 years and 10 months old'
str=str1.split(" ")
print(str)
list=[]
for i in str:
    if i.isdigit():
        list.append(i)
print(list)
res=''.join(list)
print(res)