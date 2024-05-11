str="nar@ya@#$%^na"
import string

lower=string.ascii_lowercase

count=0
for i in str:
    if i not in lower:
        count=count+1
print(count)

str1=[]
for i in str:
    if i in lower:
      str1.append(i)
print(str1)
str2=''.join(str1)
print(str2)