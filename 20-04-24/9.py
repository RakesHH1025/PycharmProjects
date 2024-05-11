list=[1,2,3,4,5,6,7,8,9]
fst=list.pop(0)
lst=list.pop(-1)

list.append(fst)
list.insert(0,lst)
print(list)