list=["geeks","for","geeks"]
count=0
for i in range(0,len(list)):
    if list[i]=="geeks":
        count=count+1
    if count==2:
        del list[i]
print(list)