list=[1,2,34,56,7,8,9]
max=list[0]
min=list[0]
for i in range(1,len(list)):
    if list[i]>max:
        max=list[i]
print(max)

for i in range(1,len(list)):
    if list[i]<min:
        min=list[i]
print(min)