list=[5,2,8,7,9,10]
print([i*i for i in list if i%2==0])

for i in list:
    i=i*i
    if i%2==0:
        print(i)
