numbers = [1, 2, 3, 4, 5, 6, 7]
res=[]
for i in numbers:
    res.append(i*i)
print(res)

res=[i*i for i in numbers]
print(res)