str="Python Narayana Tech House Hyd"
str1=str.split()
print(str1)


newlist=[]
for i in str1:
    if len(i)%2==0:
        newlist.append(i)
print(newlist)