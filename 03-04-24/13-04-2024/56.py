l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3=[]
for i in l1[1::2]:
    l3.append(i)
for i in l2[0::2]:
    l3.append(i)
print(l3)