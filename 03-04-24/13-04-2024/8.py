mylist=[10,15,20,25,30,35]
# mylist[0],mylist[-1]=mylist[-1],mylist[0]

# get=(mylist[-1],mylist[0])
# mylist[0],mylist[-1]=get
# print(mylist)

first=mylist.pop(0)
last=mylist.pop(-1)

mylist.append(first)
mylist.insert(0,last)
print(mylist)