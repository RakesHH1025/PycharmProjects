numbers=[1,2,3,4,5,6,7,11,12,15]
number=[]
for i in range(1,16):
    if i not in numbers:
        number.append(i)
print(number)
