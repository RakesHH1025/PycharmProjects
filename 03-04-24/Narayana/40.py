list=[18,4,7,10,16,9,20,11,15]
minnum=min(list)
maxnum=max(list)
print([i for i in range(minnum+1,maxnum) if i not in list])

for i in range(minnum+1,maxnum):
    if i not in list:
        print(i,end=" ")