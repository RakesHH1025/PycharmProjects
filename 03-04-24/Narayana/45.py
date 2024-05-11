list=[1,2,2,3,4,5,4,3,4]
print([i for i in list if list.count(i)==1])

for i in list:
    if list.count(i)==1:
        print(i)