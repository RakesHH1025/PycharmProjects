numbers=[1,2,3,4,4,5,5,6,7,8,8,89,10,1,2,2,2,3,3,1]
number=[]
for i in numbers:
    if i not in number:
        number.append(i)
print(number)

res=dict()
for i in numbers:
    count=numbers.count(i)
    res[i]=count
print(res)