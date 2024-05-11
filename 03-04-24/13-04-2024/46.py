str1 = "PyNaTive"
upper=[]
lower=[]
for i in str1:
    if i.isupper():
        upper.append(i)
    else:
        lower.append(i)
res="".join(lower+upper)
print(res)