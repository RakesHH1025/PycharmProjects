str="Austerila won more worldcups than india"
str1=str.split()
newlist=[]

for i in str1:
    if i[0].lower() in 'aeiou' and i[-1] in 'aeiou':
        newlist.append(i)
print(newlist)