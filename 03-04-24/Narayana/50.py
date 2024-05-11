str='python narayana and python developer and python tester'
str=str.split()
s=set(str)
d={}.fromkeys(s,0)
for i in str:
    if i in d:
        d[i]=d[i]+1
print(d)

for i in d:
    if d[i] == max(d.values()):
        print(i)