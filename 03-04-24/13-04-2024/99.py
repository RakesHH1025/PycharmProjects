list=[11,1,2,3,4,56,7,8,9,7,8,9,4,5,6,1,2]
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)

fm=max(list[0],list[1])
sm=min(list[0],list[1])

for i in range(2,len(list)):
    if list[i]>fm:
        sm=fm
        fm=sm
    elif list[i]>sm:
        sm=list[i]
print(sm)