list=[10,20,30,10,20,30,40,50,10,20,20,20,20,10,40]
s=set(list)
d={}.fromkeys(s,0)
for i in list:
    d[i]=d[i]+1

for i in d:
    if d[i] == max(d.values()):
        print(i)