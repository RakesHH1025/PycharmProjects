list=[10,5,20,15,30,8]

a=0
for i in list:
    if i>a:
        a=i
print(a)


b=0
for j in list:
    if j>b and j<a:
        b=j
print(b)
