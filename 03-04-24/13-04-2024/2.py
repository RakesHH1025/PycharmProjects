num=15
count=0

for i in range(1,num+1):
    if (num%i==0):
        count=count+1
if count==2:
    print("prime")
else:
    print("Not prime")