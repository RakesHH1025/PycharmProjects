str="Austerila won more worldcups than india"
str=str.split()
v='aeiou'
reslist=[ ]
for i in str:
    if i[0].lower() in v and i[-1] not in v:
        reslist.append(i)
print(reslist)