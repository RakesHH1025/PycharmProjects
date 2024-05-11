str="python narayana tech house"
str.split()
for i in str:
    if i[0] in "aeiou":
        print(i,end=" ")