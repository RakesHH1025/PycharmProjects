str="narayana tech house"
v='aeiou'
d={}.fromkeys(v,0)

for i in str:
    if i in d:
        d[i]=d[i]+1

print(d)

