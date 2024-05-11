mylist=[10,15,20,25,30,35]
x=10
count=0
for i in mylist:
    if i==x:
        count=count+1
print(count)
print(mylist.count(x))


from collections import Counter

dict=Counter(mylist)

print(dict)