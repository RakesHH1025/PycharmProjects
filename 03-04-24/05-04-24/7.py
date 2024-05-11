str="python narayana tech house hyd"
str1=str.split()
newlist=[]
for i in str1:
    if len(i)%2==0:
        newlist.append(i)
print(newlist)