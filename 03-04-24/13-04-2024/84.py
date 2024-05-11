numbers=[1,2,3,4,4,5,5,6,7,8,8,89,10,1,2,2,2,3,3,1]
max=numbers[0]
min=numbers[0]
for i in range(0,len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
print(max)

for i in range(0,len(numbers)):
    if numbers[i]<min:
        min=numbers[i]
print(min)