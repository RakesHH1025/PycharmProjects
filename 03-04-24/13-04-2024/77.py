name='RAKESHRUSHITHA'
matchingchars=[]
for i in name:
    if (name.count(i)>1):
        matchingchars.append(i)
print(matchingchars)

res=dict()
for i in name:
    count=name.count(i)
    res[i]=count
print(res)