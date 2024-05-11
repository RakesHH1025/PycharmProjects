list=[10,5,9,15,25,20]

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]

print(list)

