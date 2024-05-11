l=["Rakesh","suresh",2234,"ramu",542,1234]
names=[]
numbers=[]
for i in l:
    if type(i)==str:
        names.append(i)
    if type(i)==int:
        numbers.append(i)
print(names)
print(numbers)