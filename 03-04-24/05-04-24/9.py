str="python narayana tech house"
str=str.split()
newlist=[]
for i in str:
    if i[0] not in "aeiou" and i[-1] in "aeiou":
        newlist.append(i)
print(newlist)

# str = "python narayana tech house"
# str = str.split()
# newlist = []
#
# for word in str:
#     if word[0] in "aeiou" and word[-1] in "aeiou":
#         newlist.append(word)
#
# print(newlist)
