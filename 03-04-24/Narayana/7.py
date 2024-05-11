str="narayana"
str1=set(str)
d={}.fromkeys(str1,0)

for i in str1:
    d[i]=d[i]+1
print(d)