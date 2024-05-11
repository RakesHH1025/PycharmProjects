mylist=[10,15,20,25,30,35]
max=mylist[0]
min=mylist[0]
for i in range(0,len(mylist)):
    if mylist[i]>max:
        max=mylist[i]
print(max)

for i in range(0,len(mylist)):
    if mylist[i]<min:
        min=mylist[i]
print(min)